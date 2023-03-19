from cassandra.cluster import Cluster

cluster = Cluster()
connection = cluster.connect('people')
results = connection.execute('SELECT * FROM employees')
for row in results:
    print(row.id, row.name, row.city, row.hire_date)