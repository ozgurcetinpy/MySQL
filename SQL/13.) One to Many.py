import mysql.connector

def GetProducts():
    connection = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "node-app"
    )

    cursor = connection.cursor()

    # sql = "SELECT * from products"
    # sql = "SELECT * from categories"
    # sql = "SELECT * from products INNER JOIN categories ON categories.id = products.categoryid"
    # sql = "SELECT products.name,products.price,categories.name from products INNER JOIN categories ON products.categoryid = categories.id"
    # sql = "SELECT products.name,products.price,categories.name from products INNER JOIN categories ON products.categoryid = categories.id WHERE categories.name = 'bilgisayar' " 
    # sql = "SELECT products.name,products.price,categories.name from products INNER JOIN categories ON products.categoryid = categories.id WHERE products.name = 'Asus Rog' "
    sql = "SELECT p.name,p.price,c.name from products as p INNER JOIN categories as c ON p.categoryid = c.id WHERE c.name = 'bilgisayar' "

    cursor.execute(sql)

    try:
        result =cursor.fetchall()
        for i in result:
            print(i)
    except mysql.connector.Error as Err:
        print("Hata oluştu : ",Err)
    finally:
        connection.close()
        print("Veritabanı Kapandı")

GetProducts()