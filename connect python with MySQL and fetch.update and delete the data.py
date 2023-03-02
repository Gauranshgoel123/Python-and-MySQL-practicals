import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create a cursor object to execute queries
mycursor = mydb.cursor()

# Fetch data from table
mycursor.execute("SELECT * FROM yourtable")
result = mycursor.fetchall()

# Print the fetched data
for row in result:
  print(row)

# Update data in table
mycursor.execute("UPDATE yourtable SET column1 = 'new_value' WHERE id = 1")
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# Delete data from table
mycursor.execute("DELETE FROM yourtable WHERE id = 2")
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
