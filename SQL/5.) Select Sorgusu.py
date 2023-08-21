import re
import mysql.connector

def GetProducts():
    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )

    cursor = conneciton.cursor()

    # cursor.execute("SELECT * from products")
    cursor.execute("SELECT isim,price from products")

    # result = cursor.fetchall()            # listedeki bütün satırları getirir
    result = cursor.fetchone()              # listeden bir satır getirir.
    print(f"name = {result[0]}, price = {result[1]}")

    # for product in result:
    #     print(f"name = {product[1]}, price = {product[2]}")         # Bir tane kayıt kullanıcaksak dögüye gerek yok
    #     print(f"name = {product[0]}, price = {product[1]}")
    #     print(product)

GetProducts()