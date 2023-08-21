from re import S
from types import MethodType
import mysql.connector
import datetime

from mysql.connector import cursor
from conneciton import connection

class Student:
    # Cursor ve Connection gibi bilgiler classa özel bir tane olmalı
    connection = connection
    cursor = connection.cursor()


    def __init__(self,studentnumber,studentname,studentsurname,birthdate,studentgender):
        self.studentnumber = studentnumber
        self.studentname = studentname
        self.studentsurname = studentsurname
        self.birthdate = birthdate
        self.studentgender = studentgender


    def SaveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,StudentName,StudentSurname,BirthDate,StudentGender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentnumber,self.studentname,self.studentsurname,self.birthdate,self.studentgender) 
        Student.cursor.execute(sql,value)

        print("Eklenen kayıt sayısı = {}".format(Student.cursor.rowcount))
        print("Son eklenen KAydın id numarası = {}".format(Student.cursor.lastrowid))

        try:
            Student.connection.commit()
        except mysql.connector.Error as err:
            print("Hata oluştu = {}".format(err))
        finally:
            Student.connection.close()
            print("Veritabanı kapandı")


    @staticmethod
    def SaveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,StudentName,StudentSurname,BirthDate,StudentGender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.cursor.executemany(sql,values)

        print("Eklenen kayıt sayısı = {}".format(Student.cursor.rowcount))
        print("Son eklenen KAydın id numarası = {}".format(Student.cursor.lastrowid))

        try:
            Student.connection.commit()
        except mysql.connector.Error as err:
            print("Hata oluştu = {}".format(err))
        finally:
            Student.connection.close()
            print("Veritabanı kapandı")


    @staticmethod
    def StudentInfo_a():
        sql = "SELECT * from student"
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()
    
    @staticmethod
    def StudentInfo_b():
        sql = "SELECT id,StudentName,StudentSurname from student"
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()

    # Kadınların adı ve soyadı

    @staticmethod
    def StudentInfo_c():
        sql = "SELECT StudentName,StudentSurname from student Where StudentGender = 'Kadın' "
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()      

    # Doğum Yılı 1999 olanlar
    
    @staticmethod
    def StudentInfo_d(): 
        sql = "SELECT * from student WHERE YEAR(BirthDate) = 1999"     # YEAR, MONTH, DAY ==> yıl, ay gün bilgilerini alabiliriz.      
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()

    # Adı "inci" ve doğum yılı 2000 olanlar

    @staticmethod
    def StudentInfo_e():
        sql = "SELECT * from student WHERE StudentName = 'İnci' and YEAR(BirthDate) = 2000 "
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()

    #isminde ya da soyisminde "an" geçenler

    @staticmethod
    def StudentInfo_f():
        sql = "SELECT * from student WHERE StudentName LIKE  '%in%' or StudentSurname LIKE  '%in%' "    # LIKE ifadesinde "=" kullanılmaz.
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()

    # Kaç erkek öğrenci vardır

    @staticmethod
    def StudentInfo_g():
        sql = "SELECT COUNT(StudentGender) from student WHERE StudentGender = 'Erkek' "
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchone()
            print(result)
            # for i in result:
            #     print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()
    
    #Kız öğrencileri isme göre sırala

    @staticmethod
    def StudentInfo_h():
        sql = "SELECT * from student WHERE StudentGender = 'Kadın' ORDER BY StudentName,StudentSurname"
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()
    

    # Limit Kaydı
    @staticmethod
    def StudentInfo_ı():
        sql = "SELECT * from student LIMIT 5"
        Student.cursor.execute(sql)

        try:
            result = Student.cursor.fetchall()
            for i in result:
                print(i)
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            print("Veriler işleniyor...")
            Student.connection.close()
    



Student.StudentInfo_h