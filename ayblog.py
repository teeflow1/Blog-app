import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Bimbo4wife'
)

# Prepare a cursor objects

cursorObject = database.cursor()

# create a database

cursorObject.execute("CREATE DATABASE bloggy")


print("Good Job Ayo")