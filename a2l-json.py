import sys
import json
import re

text_template = '''    /begin MEASUREMENT {var_name} ""
      {var_type} NO_COMPU_METHOD 0 0 0 65535
      READ_WRITE
      ECU_ADDRESS {var_addr}
      ECU_ADDRESS_EXTENSION 0x0
      FORMAT "%.15"
      MATRIX_DIM {array}
      LAYOUT ROW_DIR
      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP {var_name} {var_addr} 0x0 0 0x0 1 0x87 0x0
        DISPLAY 0 0 65535
      /end IF_DATA
      SYMBOL_LINK {var_name} 0
    /end MEASUREMENT\n
    /begin COMPU_METHOD {var_name}.CONVERSION ""
      LINEAR "%3.1" ""
      COEFFS_LINEAR {conv} 0
    /end COMPU_METHOD\n'''
    
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
        a2l_text = '''ASAP2_VERSION 1 61\n/* generated a2l */\n/begin PROJECT Example ""\n  /begin MODULE CCP ""\n'''
        for v in self.dic_var:
            m = re.search(r'(\[(?P<x>\d+)\])(\[(?P<y>\d+)\])?(\[(?P<z>\d+)\])?', v['array'])
            if m:
                x = m.group('x') if m.group('x') else 1
                y = m.group('y') if m.group('y') else 1
                z = m.group('z') if m.group('z') else 1
                array = '{0} {1} {2}'.format(x, y, z)

            m = re.search(r'{0}\s+(0x[0-9a-fA-F]{{8}})'.format(v['name']), self.mapdata)
            if m:
                var_addr = m.group(1)
            else:
                var_addr = '0x0'

            text = text_template.format(
                var_name=v['name'],
                var_type=self.dic_type[v['type']],
                array=array,
                var_addr=var_addr,
                conv=v['conv']
            )
            a2l_text += text

        a2l_text += '''\n/end PROJECT\n''' 

        with open(a2l_fname, 'w') as f:
            f.write(a2l_text)

if __name__=='__main__':
    aj = AsapJson()
    aj.from_json('variable.json', 'variable.map')
    aj.to_a2l('template.a2l')

