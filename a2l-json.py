import sys
import json
import re

a2l_start = '''/* @@@@ File written by a2l-json @@@@ */\n
ASAP2_VERSION 1 61\n
/begin PROJECT Example ""\n
  /begin MODULE CCP ""\n\n'''
a2l_end = '''  /end MODULE\n/end PROJECT\n''' 
measure_template = '''    /begin MEASUREMENT {var_name} ""
      {var_type} NO_COMPU_METHOD 0 0 0 65535
      READ_WRITE
      ECU_ADDRESS {var_addr}
      ECU_ADDRESS_EXTENSION 0x0
      FORMAT "%.15"
      MATRIX_DIM {array}
      LAYOUT ROW_DIR
      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP "{var_name}{_0_}" {var_addr} 0 0 0 0 0 0
        DISPLAY 0 0 65535
      /end IF_DATA
      SYMBOL_LINK "{var_name}{_0_}" 0
    /end MEASUREMENT\n\n'''

conv_template = '''    /begin COMPU_METHOD {var_name}.CONVERSION ""
      LINEAR "%3.1" ""
      COEFFS_LINEAR {conv} 0
    /end COMPU_METHOD\n\n'''

item_template = '''{indent}/begin {ID} {ID_NAME} {comment}
{contents}{indent}/end {ID}\n'''
    
def read_jsonc(fname):
    with open(fname, 'r') as f:
        try:
            return json.loads(re.sub("//.*","",f.read(),flags=re.M))
        except:
            print('Invalid json format : {0}'.format(fname))
            sys.exit(1)
def read_file(fname):
    with open (fname, 'r') as f:
        return f.read()
        
class AsapJson:
    def from_json(self, json_fname, map_fname=''):
        dic_con = read_jsonc(json_fname)
        if map_fname:
            self.mapdata = read_file(map_fname)

        self.dic_var = dic_con['variable']
        self.dic_type = dic_con['type']
        self.dic_size = dic_con['type_size']

    def to_a2l(self, a2l_fname):
        def set_contents_from_list(key, dictionary, indent=4):
            if key in dictionary:
                return item_template.format(
                            indent=' '*indent,
                            ID=key,
                            ID_NAME='',
                            comment='',
                            contents=set_contents(dictionary[key], indent+2))
            else:
                return ''

        def set_template_item(item, key, contents, indent=4):
            return item_template.format(
                    indent=' '*indent,
                    ID=item,
                    ID_NAME=key,
                    comment='""',
                    contents=contents) + '\n'

        def set_contents(list_item, indent=4):
            return ''.join(['{s}{0}\n'.format(d, s=' '*indent) for d in list_item])
        def set_content(text, indent=6):
            return '{s}{0}\n'.format(text, s=' '*indent)
        def set_link_map(text, indent=6):
            return '{s}/begin IF_DATA CANAPE_EXT\n{s2}100\n{s2}LINK_MAP "{0}" 0 0 0 0 0 0 0\n{s}/end IF_DATA\n'.format(
                    text, s=' '*indent, s2=' '*(indent+2))
        a2l_text = a2l_start 

        set_group = set()
        dic_g = {}
        for v in self.dic_var:
            var_name = v['name']

            _0_ = ''
            if 'array' in v:
                m = re.search(r'(\[(?P<x>\d+)\])(\[(?P<y>\d+)\])?(\[(?P<z>\d+)\])?', v['array'])
                if m:
                    x = int(m.group('x')) if m.group('x') else 1
                    y = int(m.group('y')) if m.group('y') else 1
                    z = int(m.group('z')) if m.group('z') else 1
                    
                    _0_ += '._0_' if x > 1 else ''
                    _0_ += '._0_' if y > 1 else ''
                    _0_ += '._0_' if z > 1 else ''
                    array = '{0} {1} {2}'.format(x, y, z)
            else:
                array = ''

            m = re.search(r'{0}\s+(0x[0-9a-fA-F]{{8}})'.format(var_name), self.mapdata)
            if m:
                var_addr = m.group(1)
            else:
                var_addr = '0x0'

            var_type = self.dic_type[v['type']]

            if 'A2L_TYPE' in v:
                if v['A2L_TYPE'] == 'STRING':
                    contents = set_content('ASCII {var_addr} __{var_type}_Z 0 NO_COMPU_METHOD 0 255'.format(
                        var_addr=var_addr,
                        var_type=var_type))
                    contents += set_content('NUMBER {0}'.format(x))
                    contents += set_link_map(var_name)
                    text = set_template_item('CHARACTERISTIC', var_name, contents)
                elif v['A2L_TYPE'] == 'MAP':
                    contents = set_content('MAP 0 RL_{0} 0 NO_COMPU_METHOD 0 255'.format(var_type))
                    contents += set_content('NUMBER {0}'.format(x))
                    contents += set_link_map(var_name)
                    text = set_template_item('CHARACTERISTIC', var_name, contents)
            else:
                text = measure_template.format(
                    var_name=var_name,
                    var_type=var_type,
                    array=array,
                    var_addr=var_addr,
                    _0_=_0_
                )
            if 'conv' in v:
                text = text.replace('NO_COMPU_METHOD', var_name+'.CONVERSION')
                text += conv_template.format(
                var_name=var_name,
                conv=v['conv']
            )

            def append_value(dict_obj, key, value):
                if key not in dict_obj:
                    dict_obj[key] = [value]
                else:
                    dict_obj[key].append(value)

            if 'group' in v:
                root_group, list_sub_group = v['group'].split('/')[0], v['group'].split('/')
                
                # GROUP
                if root_group not in dic_g:
                    dic_g[root_group] = {'type' : 'GROUP'}

                # SUB_GROUP
                for idx, val in enumerate(list_sub_group):
                    if val not in dic_g:
                        dic_g[val] = {'type' : 'SUB_GROUP'}
                    if idx+1 < len(list_sub_group):
                        append_value(dic_g[val], 'SUB_GROUP', list_sub_group[idx+1])
                # variable
                if 'A2L_TYPE' in v:
                    append_value(dic_g[list_sub_group[-1]], 'REF_MEASUREMENT', var_name)
                else:
                    append_value(dic_g[list_sub_group[-1]], 'REF_CHARACTERISTIC', var_name)
            a2l_text += text

        group_text = ''
        for key in dic_g:
            contents = ''
            if dic_g[key]['type'] == 'GROUP':
                contents = set_content('ROOT')
            
            for con_list in ['SUB_GROUP','FUNCTION_LIST','REF_CHARACTERISTIC','REF_MEASUREMENT']:
                contents += set_contents_from_list(con_list, dic_g[key], indent=6)

            group_text += set_template_item('GROUP', key, contents)

        a2l_text += group_text + a2l_end

        with open(a2l_fname, 'w') as f:
            f.write(a2l_text)

if __name__=='__main__':
    aj = AsapJson()
    aj.from_json('variable.json', 'variable.map')
    aj.to_a2l('template.a2l')
