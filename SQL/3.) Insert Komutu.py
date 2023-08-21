from os import name
from re import L
import mysql.connector
from mysql.connector.fabric import connect

def InsertProduct(isim,price,imgURL,description):
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(isim, price, imgURL, description) VALUES (%s,%s,%s,%s) "
    values = (isim, price,imgURL, description)

    cursor.execute(sql,values)

    print(f"Eklenen Satır : {cursor.rowcount}")
    print(f"Son sıradaki id : {cursor.lastrowid}")

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata oluştu : ",err)
    finally:
        connection.close()


def InsertProducts(liste):
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO Products(isim, price, imgURL, description) VALUES (%s,%s,%s,%s) "
    values = liste

    cursor.executemany(sql,values)

    print(f"Eklenen Satır : {cursor.rowcount}")
    print(f"Son sıradaki id : {cursor.lastrowid}")

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata oluştu : ",err)
    finally:
        connection.close()

liste = []
key = 1
while key == 1:
    isim = input("Telefon Adı : ")
    price = float(input("Telefonun Fiyatı : "))
    imgURL = input("Tanıtım uzantısı : ")
    description = input("Telefon hakkında açıklama : ")
    
    liste.append((isim,price,imgURL,description))
    
    result = input("Devam etmek istiyor musunuz ? (e/h)")
    if result == "h":
        print("Kayıt yapılıyor...")
        print(liste)
        InsertProducts(liste)
        key = 0
    