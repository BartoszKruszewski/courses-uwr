import os
import xml.etree.ElementTree as ET

from jinja2 import Environment, FileSystemLoader

tree = ET.parse('classes.xml')
env  = Environment(loader=FileSystemLoader('.'))
tpl  = env.get_template('class_template.j2')

for cls in tree.findall('.//class'):
    code = tpl.render(
        name   = cls.get('name'),
        fields = [f.attrib for f in cls]
    )
    with open(f'{cls.get("name")}.py', 'w') as f:
        f.write(code + '\n')
    print('✔', cls.get('name'))
