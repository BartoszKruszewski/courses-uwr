# cd zad1
# python3 -m venv venv
# source ./venv/bin/activate
# pip install -r requirements.txt
# python3 run.py

import xml.etree.ElementTree as ET
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

root = Path(__file__).parent
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
