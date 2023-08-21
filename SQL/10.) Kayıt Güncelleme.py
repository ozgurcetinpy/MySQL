from sys import exec_prefix
import mysql.connector


def UpdateProduct(id,name,price):

    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = conneciton.cursor()

    sql = "UPDATE products SET isim = %s, price = %s WHERE id = %s "      # WHERE olmasaydı bütün satırların isimleri ip4 olurdu.
    values = (name,price,id)

    cursor.execute(sql,values)

    try:
        conneciton.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print("Hata : ",err)
    finally:
        print("veritabanı sonlandı.")
        conneciton.close()

ID = int(input("Güncellemek istediğiniz id nuamrası : "))
NAME = input("İSmi ne olarak güncellemek istersiniz : ")
PRICE = float(input("Ücreti ne olarak güncellemek isterisiniz : "))
UpdateProduct(ID,NAME,PRICE)



    

    
    