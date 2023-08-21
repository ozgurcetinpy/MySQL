import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySQLite.123",
    database = "mydatabase"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255) ) ")



