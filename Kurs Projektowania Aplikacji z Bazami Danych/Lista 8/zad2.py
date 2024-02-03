from neo4j import GraphDatabase
from connect_data import URI, USERNAME, PASSWORD

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# add 2 new actors and 2 new movies
with driver.session() as session:
    session.run("""
    CREATE
        (newActor1:Person {name: 'New Actor 1'}),
        (newActor2:Person {name: 'New Actor 2'}),
        (newMovie1:Movie {title: 'New Movie 1'}),
        (newMovie2:Movie {title: 'New Movie 2'});
    """)
    
# add 2 new properties to 1 movie
with driver.session() as session:
    session.run("""
    MATCH 
        (movie:Movie {title: 'New Movie 1'})
    SET 
        movie.newProperty1 = 'New Property Value 1',
        movie.newProperty2 = 'New Property Value 2';
    """)

# add 2 new ACTED_IN relations to the existing nodes
with driver.session() as session:
    session.run("""
    MATCH
        (actor:Person {name: 'New Actor 1'}),
        (movie:Movie {title: 'Wall Street'})
    CREATE 
        (actor)-[:ACTED_IN {role: 'New Role 1'}]->(movie);
    """)

with driver.session() as session:
    session.run("""
    MATCH
        (actor:Person {name: 'New Actor 2'}),
        (movie:Movie {title: 'New Movie 2'})
    CREATE 
        (actor)-[:ACTED_IN {role: 'New Role 2'}]->(movie);
    """)

# update 1 movie property
with driver.session() as session:
    session.run("""
    MATCH 
        (movie:Movie {title: 'Wall Street'})
    SET 
        movie.updatedProperty = 'Updated Property Value';
    """)

# remove 1 acted in relation
with driver.session() as session:
    session.run("""
    MATCH 
        (actor:Person {name: 'Charlie Sheen'})-[actedIn:ACTED_IN]->(movie:Movie {title: 'Wall Street'})
    DELETE 
        actedIn;
    """)

driver.close()
