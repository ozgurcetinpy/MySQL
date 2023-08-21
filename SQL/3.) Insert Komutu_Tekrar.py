import mysql.connector
from mysql.connector.fabric import connect

def InsertProduct():
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1" 
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products (isim, price, imgURL, description) VALUES (%s,%s,%s,%s)"
    values = ("Xiaomi Mi 5", 1500, "mi5.jpg", "eskiden kaliteli telefondu")

    cursor.execute(sql,values)
    
    connection.commit()

