from database import Graph

db = Graph('bolt://3.82.197.78:7687', 'neo4j', 'abuser-bombs-administrations')

print("Quem da familia é empreendedor")
result = db.execute_query('MATCH(n:Empreendedor) RETURN n;')
for record in result:
    print(record['n']['name'])

print("\nLuana é namora com quem desde quando?")
result1 = db.execute_query("MATCH(n:Pessoa{name:'Luana'})-[r:NAMORADA_DE]->(p) RETURN p,r;")
for record in result1:
    print(f'Luana namora com o {record["p"]["name"]} desde {record["r"]["desde"]}')

print("\nAmanda é irmão de quem?")
result2 = db.execute_query("MATCH(:Pessoa{name:'Amanda'})-[IRMAO_DE]->(p) RETURN p;")
for record in result2:
    print(record['p']['name'])
