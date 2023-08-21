import mysql.connector
from mysql.connector.fabric import connect

def GetProducts():
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )

    cursor = connection.cursor()

    # cursor.execute("SELECT * from products")     
    cursor.execute("SELECT isim, price from products")        # products tablosunda sadece isim ve price sütünlarını alır.

    urunler = cursor.fetchall()          # fatchmany(5)  ==> ilk 5 tane satırı alır
    for i in urunler:
        print(i)

GetProducts()