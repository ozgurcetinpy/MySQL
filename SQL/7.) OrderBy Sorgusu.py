import re
import mysql.connector
from mysql.connector.fabric import connect

def GetProducts():
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )

    cursor = connection.cursor()

    # sql = "SELECT * from products ORDER BY price"      # alfabetik ya da küçükten büyüğe sıralar.
    # sql = "SELECT * from products ORDER BY id DESC"      #DESC ==> Azalan, ASC ==> Artan
    sql = "SELECT * from products ORDER BY isim, price"   # isim ve kendi içinde price kategorisinde sıralama yapar.
    cursor.execute(sql)
    try:
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        print("Hata : ", err)
    finally:
        connection.close()
        print("veritabanı bağlantıs kapandı")

    for i in result:
        print(f"id = {i[0]}, name = {i[1]}, price = {i[2]}")

GetProducts()
