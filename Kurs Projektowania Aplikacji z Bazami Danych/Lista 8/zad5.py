from neo4j import GraphDatabase
from connect_data import URI, USERNAME, PASSWORD

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

def create_person(driver, name):
    with driver.session() as session:
        result = session.run("CREATE (p:Person {name: $name}) RETURN p", name=name)
        return Person(result.single()["p"].id, name)

def read_all_persons(driver):
    with driver.session() as session:
        result = session.run("MATCH (p:Person) RETURN p")
        return [Person(record["p"].id, record["p"]["name"]) for record in result]

def read_person(driver, id):
    with driver.session() as session:
        result = session.run("""
            MATCH (p:Person) 
            WHERE ID(p) = $id RETURN p
            """, id=id)
        record = result.single()
        if record:
            return Person(record["p"].id, record["p"]["name"])
        else:
            return None

def update_person(driver, id, name):
    with driver.session() as session:
        result = session.run("""
            MATCH (p:Person) WHERE ID(p) = $id
            SET p.name = $name 
            RETURN p
            """, id=id, name=name)
        return Person(result.single()["p"].id, name)

def delete_person(driver, id):
    with driver.session() as session:
        session.run("MATCH (p:Person) WHERE ID(p) = $id DELETE p", id=id)

with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
        created_person = create_person(driver, "John Doe")
        print("Created Person:", created_person.__dict__)

        all_persons = read_all_persons(driver)
        print("All Persons:", [person.__dict__ for person in all_persons])

        read_person_by_id = read_person(driver, created_person.id)
        print("Read Person by ID:", read_person_by_id.__dict__)

        updated_person = update_person(driver, created_person.id, "John Doe Updated")
        print("Updated Person:", updated_person.__dict__)

        delete_person(driver, created_person.id)
        print("Person Deleted.")

        all_persons_after_deletion = read_all_persons(driver)
        print("All Persons After Deletion:", [person.__dict__ for person in all_persons_after_deletion])
