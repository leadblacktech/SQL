#import modules
import json
import csv
from unittest import result
import mysql.connector

#connect to database
conn = mysql.connector.connect(
host='localhost',
database='database',
user='root',
password='your_password')


cursor = conn.cursor() # Create a cursor object using cursor() method
cursor.execute("SELECT * FROM your_table") # Execute the SQL command
result = cursor.fetchall() # Fetch all the rows in a list of lists.
print(result) # Print results


cursor.close() # Close the cursor
conn.close() # Close the connection

json_formatted_str = json.dumps(result, indent=4) # Format the result
print(json_formatted_str) # Print the result

#print to text file open and write
with open('filepath', 'a') as f: # Open the file
    f.write(json_formatted_str) # Write the result to the file

with open('filepath', 'a', newline='') as csvfile: # Open the file
    csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)  # write to csv, delimiter is the seperator
    csvwriter.writerow(['ID','Photo Amount','Name','Description','Quality','Location','Link','Printed','Hours','Date Taken'])
    csvwriter.writerow([result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], result[0][9]]) 
    csvwriter.writerow([result[1][0], result[1][1], result[1][2], result[1][3], result[1][4], result[1][5], result[1][6], result[1][7], result[1][8], result[1][9]])
    csvwriter.writerow([result[2][0], result[2][1], result[2][2], result[2][3], result[2][4], result[2][5], result[2][6], result[2][7], result[2][8], result[2][9]])
    