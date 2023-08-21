import mysql.connector

def ProductInfo():
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "node-app"
    )
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) from products WHERE price > 2000"       # ==> COUNT, kaç satır olduğunu sayar
    # sql = "SELECT AVG(price) from products"                        # ==> AVG, ait olduğu sününü ortalamsını alır ve geriye döndürür.
    # sql = "SELECT SUM(price) from products"                        # ==> SUM, ait olduğu sütünların değerlerini toplar
    # sql = "SELECT MIN(price) from products"                        # ==> MIN, miniumum değeri gösterir. 
    # sql = "SELECT MAX(price) from products"                        # ==> MAX, maximum değeri gösterir.
    sql = "SELECT name from products WHERE price = (SELECT MIN(price) from products)"  # En pahalı ürünün ismi ne ? 

    cursor.execute(sql)

    result = cursor.fetchall()
    print(result)

ProductInfo()
