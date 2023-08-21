import mysql.connector

connection = mysql.connector.connect(   # Burada Server ile bağlanıta geçildi
    host = "localhost",
    user = "root",
    password = "MySQLite.123",
    database = "schooldb"         #Burada ise database ile bağlanıtya geçildi.
) 

my_cursor = connection.cursor()   # Bir tane Cursor oluşturdum

my_cursor.execute("Show Databases")    #Database komutları ile Cursor'den istediğimiz bilgiye erişebilir.

for i in my_cursor:
    print(i)
