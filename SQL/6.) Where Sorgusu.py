import mysql.connector

def GetProducts():
    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = conneciton.cursor()

    # cursor.execute("SELECT * from products  WHERE isim = 'mi5' or price = 3000 ") 
    # cursor.execute("SELECT * from products WHERE isim LIKE '% mi %' ")       #  ==> isim alanında 'mi' geçen kayıtları bana listele
    # cursor.execute("SELECT * from products WHERE isim LIKE 'mi%' and price >= 3000 ")     # ==>  başı 'm' ile başlayacak gerisi öenmli değil'
    # result = cursor.fetchall()   #   ==> Koşulları sağlayan bütün elemanlar LİSTE içinde TUPLE değişkeni olarak gelir.
    cursor.execute("SELECT * from products WHERE id = 4")
    result = cursor.fetchall()    # ==>  Koşulu sağlayan ilk satır tuple olarak gelir çünkü fetchone ile çağırıldı, listeye gerek yok.

    print(result)
    # for i in result:
    #     print(f"id = {i[0]}, name = {i[1]}, price = {i[2]}")





def GetProductByID(id):
    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = conneciton.cursor()
    sql = "SELECT * from products WHERE id = %s"
    value = (id,)           

    cursor.execute(sql,value)
    result = cursor.fetchone()

    print(f"id = {result[0]}, name  = {result[1]}, price = {result[2]}")


GetProductByID(5)