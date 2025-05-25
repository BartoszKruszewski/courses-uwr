# cd zad2
# python3 -m venv venv
# source ./venv/bin/activate
# pip install -r requirements.txt
# python3 run.py

from database import Base, engine, session_scope
from models import Child, Parent

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with session_scope(desktop=True) as s:
        p = Parent(name="Alicja")
        p.children.append(Child(name="Basia"))
        p.children.append(Child(name="Celina"))
        s.add(p)

    with session_scope(desktop=False) as s:
        result = s.query(Parent).first()
        print(result, result.children)
