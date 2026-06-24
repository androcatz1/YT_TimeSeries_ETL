from database.connection import get_connection

client = get_connection()

query = "SELECT 1 as test"

for row in client.query(query).result():
    print(row.test)