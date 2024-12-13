import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd ='Root@1'
	)

# preparing the cursor object
cursorObject = dataBase.cursor()

# Creating the database
cursorObject.execute("CREATE DATABASE emerico")

print("setup complete")