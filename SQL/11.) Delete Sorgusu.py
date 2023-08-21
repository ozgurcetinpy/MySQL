import mysql.connector

def DeleteProduct(id):
    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = conneciton.cursor()

    sql = "DELETE from products WHERE id = %s "   
    value = (id,)
    cursor.execute(sql,value)

    try:
        conneciton.commit()
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as err:
        print("Hata : ",err)
    finally:
        print("veritabanı sonlandı.")
        conneciton.close()
ID = int(input("Silmek istediğiniz id numarası : "))
DeleteProduct(ID)