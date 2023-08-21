from os import close
from re import L
import mysql.connector

def InsertProduct(name,price,imgURL,description):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "MySQLite.123", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imgURL,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imgURL,description)

    cursor.execute(sql,values)
    try:
        connection.commit()              # Veritabanının kapatmak için gerekli
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Eklenen kaydın id = {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        connection.close()
        print("Database Conneciton is closed")

def InsertProducts(liste):
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "MySQLite.123", database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products (name,price,imgURL,description) VALUES (%s,%s,%s,%s)"
    values = liste

    cursor.executemany(sql,values)     # Birden fazla kayıt eklemek istersek
    liste_1 = cursor.executemany(sql,values)
    try:
        connection.commit()              # Veritabanının kapatmak için gerekli
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Eklenen kaydın id = {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata", err)
    finally:
        print("liste_1",liste_1)
        connection.close()
        print("Database Conneciton is closed")

liste = []
while True:
    name = input("Ürün Adı : ")
    price = float(input("Ürünün Fiyatı : "))
    imgURL = input("Ürünün Resmi : ")
    description = input("Ürünün Açıklaması : ")

    liste.append((name,price,imgURL,description))

    result = input("Devam etmek istiyor musunuz ?   (e/h) ")
    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor.")
        print(liste)
        InsertProducts(liste)
        break



InsertProduct(name,price,imgURL,description)

