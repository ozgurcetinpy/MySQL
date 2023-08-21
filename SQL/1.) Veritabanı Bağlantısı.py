import mysql.connector

connection = mysql.connector.connect(host = "localhost", user = "root", password = "MySQLite.123", database = "database_1")
cursor = connection.cursor()

# cursor.execute("CREATE DATABASE Database_1")     ==> cursor objesi üzerinden database oluşturuldu.

cursor.execute ("CREATE TABLE Table_Deneme (name VARCHAR(55) , adress VARCHAR(55) )")



