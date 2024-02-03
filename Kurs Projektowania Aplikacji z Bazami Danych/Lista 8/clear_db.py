from neo4j import GraphDatabase
from connect_data import URI, USERNAME, PASSWORD

with GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD)) as driver:
    with driver.session() as session:
        query = """
        MATCH (n) DETACH DELETE n
        """
        
        session.run(query)