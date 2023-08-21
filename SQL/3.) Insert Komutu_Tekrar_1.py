from os import error
import mysql.connector
from mysql.connector.errors import Error

def InsertProducts(liste):
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )

    cursor = connection.cursor()

    sql = "INSERT INTO products (isim, price, imgURL, description) VALUES (%s,%s,%s,%s)"
    values = liste

    cursor.executemany(sql,values)
    print(f"Girilen veri sayısı = {cursor.rowcount}")
    print(f"En son girilen id numarası = {cursor.lastrowid}")

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("Hata oluştu : {}".format(err))
    finally:
        connection.close()

liste = []
while True:
    isim = input("Telefonun adını giriniz : ")
    price = float(input("telefonun fiyatını giriniz : "))
    imgURL = input("Telefonun uzantısını giriniz : ")
    description = input("Telefonun açıklaması : ")

    liste.append((isim,price,imgURL,description))

    sonuc = input("Devam etmek istiyor musunuz ? ")
    print("Evet için (e), Hayır için (h)")
    if sonuc == "h":
        print("Veriler işleniyor...")
        print(liste)
        InsertProducts(liste)
        break


