import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mike158313401!",
)

# Prepare a cursor object using cursor() method
cursorObject = database.cursor()

# Create a database in MySQL server
cursorObject.execute("CREATE DATABASE mikedb")

print("Database is created successfully.")