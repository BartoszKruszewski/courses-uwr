from neo4j import GraphDatabase
from connect_data import URI, USERNAME, PASSWORD

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# return the movies where person A acted in
with driver.session() as session:
    print(session.run('''
        MATCH (p:Person {name: 'Michael Douglas'})-[:ACTED_IN]->(m:Movie)
        RETURN m.title
    ''').values())

# return the movies where person A was both the actor and the director
with driver.session() as session:
    print(session.run('''
        MATCH (p:Person {name: 'Person A'})-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(p)
        RETURN m.title
    ''').values())

# return actors who didn’t play in any movie
with driver.session() as session:
    print(session.run('''
        MATCH (p:Person)
        WHERE NOT (p)-[:ACTED_IN]->(:Movie)
        RETURN p.name
    ''').values())

# return actors who played in more than 2 movies
with driver.session() as session:
    print(session.run('''
        MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
        WITH p, count(m) AS movieCount
        WHERE movieCount > 2
        RETURN p.name
    ''').values())

# return movies with the larger number of actors
with driver.session() as session:
    print(session.run('''
        MATCH (m:Movie)<-[:ACTED_IN]-(p:Person)
        WITH m, count(p) AS actorCount
        ORDER BY actorCount DESC
        RETURN m.title, actorCount
    ''').values())

driver.close()