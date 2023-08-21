from re import L, S
from types import MethodType
import mysql.connector
import datetime
from conneciton import connection

class Student:
    # Cursor ve Connection gibi bilgiler classa özel bir tane olmalı
    connection = connection
    cursor = connection.cursor()


    def __init__(self,id,studentnumber,studentname,studentsurname,birthdate,studentgender):
        if id is None:
            self.id = 0
        else:
            self.id = id
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

# id ' ye göre aldığınız bir öğrenicinin bilgilerini güncelleyiniz.

    @staticmethod
    def GetStudent(id):
        sql = "SELECT * from student WHERE id = %s" 
        value = (id,)

        Student.cursor.execute(sql,value)

        try:
            obj =  Student.cursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print("Hata : ",err)
        


    def UpdateStudent(self):
        sql = "UPDATE student SET StudentNumber = %s,StudentName = %s,StudentSurname = %s,BirthDate = %s,StudentGender = %s WHERE id = %s"
        values = (self.studentnumber,self.studentname,self.studentsurname,self.birthdate,self.studentgender,self.id)
        
        Student.cursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            Student.connection.close()
            print("Veritabanı kapandı.")


    @staticmethod
    def UpdateStudents(liste):
        sql = "UPDATE student SET StudentNumber = %s,StudentName = %s,StudentSurname = %s,BirthDate = %s,StudentGender = %s WHERE id = %s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        
        Student.cursor.executemany(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            Student.connection.close()
            print("Veritabanı kapandı.")



    @staticmethod
    def GetStudensGender(studensgender):
        sql = "SELECT * from student WHERE StudentGender = %s" 
        value = (studensgender,)

        Student.cursor.execute(sql,value)

        try:
            return Student.cursor.fetchall()
        except mysql.connector.Error as err:
            print("Hata : ",err)


students = Student.GetStudensGender("Erkek")
print(students)

liste = []
for std in students:
    std = list(std)
    std[2] = "Mr " + std[2]
    liste.append(std)

Student.UpdateStudents(liste)
