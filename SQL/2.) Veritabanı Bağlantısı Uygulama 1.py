import mysql.connector
from mysql.connector.fabric import connect

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQLite.123",
    database = "schooldb_1"
)

cursor = connection.cursor()

#cursor.execute("CREATE DATABASE schooldb_1")
