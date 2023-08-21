import mysql.connector

def GetProductByID(id):
    conneciton = mysql.connector.connect(
        host = "localhost", user = "root", password = "MySQLite.123", database = "database_1"
    )
    cursor = conneciton.cursor()

    sql = "SELECT * from products WHERE id = %s"
    values = (id,)

    cursor.execute(sql,values)
    result = cursor.fetchone()
    print(result)

GetProductByID(5)