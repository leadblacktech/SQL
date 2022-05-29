#importing modules
#importing mysql.connector
#conn defines the connection to the database

from unittest import result
import mysql.connector
conn = mysql.connector.connect(
host='localhost',
database='db_here',
user='root',
password='pawword')

#creating a cursor

cursor = conn.cursor()
cursor.execute("SELECT * FROM table_here")
result = cursor.fetchall()
print(result)