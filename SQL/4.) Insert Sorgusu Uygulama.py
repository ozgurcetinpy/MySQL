from re import S
from types import MethodType
import mysql.connector
import datetime
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


ogrenciler = [
    ("105","Kerim","Durmuş",datetime.datetime(1998,6,7),"Erkek"),   
    ("154","Fatih","Çifçi",datetime.datetime(1998,7,6),"Erkek"),
    ("145","Serap","Doğan",datetime.datetime(1998,1,11),"Kadın"),
    ("167","Cemre","Duran",datetime.datetime(1998,3,1),"Kadın"),
    ("197","Cem","Kaan",datetime.datetime(1998,4,5),"Erkek")
]

Student.SaveStudents(ogrenciler)







# ogrenci_1 = Student("202","Ahmet","Yılmaz",datetime.datetime(2001,5,15),"Erkek")
# ogrenci_1.SaveStudent() 



    


