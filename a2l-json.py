import sys
import json
import re

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
        LINK_MAP "{var_name}._0_" {var_addr} 0x0 0 0x0 1 0x87 0x0
        DISPLAY 0 0 65535
      /end IF_DATA
      SYMBOL_LINK "{var_name}._0_" 0
    /end MEASUREMENT\n'''
conv_template = '''
    /begin COMPU_METHOD {var_name}.CONVERSION ""
      LINEAR "%3.1" ""
      COEFFS_LINEAR {conv} 0
    /end COMPU_METHOD\n\n'''
group_template = '''    /begin GROUP {group_name} ""
{root}{variables}{sub_group}    /end GROUP\n\n'''
subgroup_template = '''      /begin SUB_GROUP
        {sub_group_list}
      /end SUB_GROUP\n'''
    
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
        a2l_text = '''/* @@@@ File written by a2l-json @@@@ */\n
ASAP2_VERSION 1 61\n
/begin PROJECT Example ""\n
  /begin MODULE CCP ""\n\n'''

        dic_group = {}
        set_group = set()
        for v in self.dic_var:
            if 'array' in v:
                m = re.search(r'(\[(?P<x>\d+)\])(\[(?P<y>\d+)\])?(\[(?P<z>\d+)\])?', v['array'])
                if m:
                    x = m.group('x') if m.group('x') else 1
                    y = m.group('y') if m.group('y') else 1
                    z = m.group('z') if m.group('z') else 1
                    array = '{0} {1} {2}'.format(x, y, z)
            else:
                array = ''

            m = re.search(r'{0}\s+(0x[0-9a-fA-F]{{8}})'.format(v['name']), self.mapdata)
            if m:
                var_addr = m.group(1)
            else:
                var_addr = '0x0'

            text = measure_template.format(
                var_name=v['name'],
                var_type=self.dic_type[v['type']],
                array=array,
                var_addr=var_addr
            )
            if 'conv' in v:
                text = text.replace('NO_COMPU_METHOD', v['name']+'.CONVERSION')
                text += conv_template.format(
                var_name=v['name'],
                conv=v['conv']
            )

            if 'group' in v:
                set_group.add('{0}/{1}'.format(v['group'], v['name']))            
            
            a2l_text += text

        dic_group = {}
        for group in set_group:
            list_group = group.split('/')
            for i in range(len(list_group)-2):
                if list_group[i] not in dic_group:
                    dic_group[list_group[i]] = {}
                if 'sub' not in dic_group[list_group[i]]:
                    dic_group[list_group[i]]['sub'] = set()
                dic_group[list_group[i]]['sub'].add(list_group[i+1])

            if list_group[-2] not in dic_group:
                dic_group[list_group[-2]] = {}
            
            if 'var' not in dic_group[list_group[-2]]:
                dic_group[list_group[-2]]['var'] = set()
            dic_group[list_group[-2]]['var'].add(list_group[-1])

        print(dic_group)

        group_text = ''
        for key in dic_group:
            if 'sub' in dic_group[key]:
                sub_group = subgroup_template.format(
                    sub_group_list='\n        '.join(dic_group[key]['sub'])
                )
            else:
                sub_group = ''

            if 'var' in dic_group[key]:
                variables = '        ' + '\n        '.join(dic_group[key]['var']) +'\n'
            else:
                variables = ''

            group_text += group_template.format(
                group_name=key,
                root='',
                variables=variables,
                sub_group=sub_group
            )

        a2l_text += group_text + '''\n  /end MODULE\n/end PROJECT\n''' 

        with open(a2l_fname, 'w') as f:
            f.write(a2l_text)

if __name__=='__main__':
    aj = AsapJson()
    aj.from_json('variable.json', 'variable.map')
    aj.to_a2l('template.a2l')

