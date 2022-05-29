from unittest import result
import mysql.connector
conn = mysql.connector.connect(
host='localhost',
database='db_here',
user='root',
password='pawword')

#creating a cursor

cursor = conn.cursor()
cursor.execute("SELECT * FROM models")
result = cursor.fetchall()
print(result)
