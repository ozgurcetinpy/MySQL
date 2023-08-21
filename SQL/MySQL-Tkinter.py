from tkinter import *
import tkinter.messagebox
import mysql.connector
from tkinter import END


root = Tk()
root.geometry("600x300")
root.title("Tkinter+MySQL")
root.resizable(0,0)
root.iconbitmap("MySQL.ico")



#DEFINE FONTS AND COLORS 
my_font = ("bold",10)
root_color = "#e3d26f"
my_color = "#2f1b25"
entry_color = "#426a5a"
button_color = "#2660a4"
button_text_color = "#f15946"


root.config(bg=root_color)

#DEFINE FUNCTIONS
def Insert():
    id = e_id.get()
    name = e_name.get()
    phone = e_phone.get()

    if (id == ""  or name == "" or phone == ""):
        tkinter.messagebox.showinfo("Insert Status","All fields are required")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password  ="MySQLite.123", database = "tkinter"
        )

        cursor = connection.cursor()

        sql = "INSERT INTO student (id,name,phone) VALUES (%s,%s,%s)"
        values = (id,name,phone)
        cursor.execute(sql,values)
        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)
        

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt eklendi")
            print("Son eklenen kaydın id numarası = {}".format(cursor.lastrowid))
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            connection.close()
            tkinter.messagebox.showinfo("Insert Status","Inserted Successfully\nDatabese closed")

def Delete():
    id = e_id.get()
    if id == "":
        tkinter.messagebox.showinfo("Delete Status","No ID number entered")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password  ="MySQLite.123", database = "tkinter"
        )

        cursor = connection.cursor()
        sql = "DELETE from student WHERE id = %s"
        value = (id,)

        cursor.execute(sql,value)
        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt silindi")
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            connection.close()
            tkinter.messagebox.showinfo("Delete Status","Deleted Successfully\nDatabese closed")

def Update():
    id= e_id.get()
    name = e_name.get()
    phone = e_phone.get()
    if (id == "" or name == "" or phone == ""):
        tkinter.messagebox.showinfo("Update Status", "All fields are required")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password  ="MySQLite.123", database = "tkinter"
        )

        cursor = connection.cursor()
    
        sql = "UPDATE student SET name = %s, phone = %s WHERE id = %s"
        values = (name,phone,id)

        cursor.execute(sql,values)

        e_id.delete(0,END)
        e_name.delete(0,END)
        e_phone.delete(0,END)

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("Hata : ",err)
        finally:
            connection.close()
            tkinter.messagebox.showinfo("Update Status","Updated Successfully\nDatabese closed")


def Get():
    id = e_id.get()
    if id == "":
        tkinter.messagebox.showinfo("Fetch Status","No ID Entered")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password  ="MySQLite.123", database = "tkinter"
        )
    
        cursor = connection.cursor()
        sql = "SELECT * from student WHERE id = %s"
        value = (id,)

        cursor.execute(sql,value)

        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0,row[1])
            e_phone.insert(0,row[2])
        
        connection.close()



#DEFINE LABELS
id = Label(root,text="Enter ID",font=my_font,fg=my_color,bg=root_color)
id.place(x=20,y=30)

name = Label(root,text="Enter Your Name",font=my_font,fg=my_color,bg=root_color)
name.place(x=20,y=60)

phone = Label(root,text="Enter Your Phone Number",font=my_font,fg=my_color,bg=root_color)
phone.place(x=20,y=90)





#DEFINE ENTRIES
e_id = Entry(fg=entry_color)
e_id.place(x= 150,y=30)

e_name = Entry(fg=entry_color)
e_name.place(x= 150,y=60)

e_phone = Entry(fg=entry_color)
e_phone.place(x= 150,y=90)



#DEFINE BUTTONS
insert_button = Button(root, text="INSERT",font=my_font,bg=button_color,fg=button_text_color,command=Insert)
insert_button.place(x=20,y=140)

delete_button = Button(root, text="DELETE",font=my_font,bg=button_color,fg=button_text_color,command=Delete)
delete_button.place(x=70,y=140)

update_button = Button(root, text="UPDATE",font=my_font,bg=button_color,fg=button_text_color,command=Update)
update_button.place(x=130,y=140)

get_button = Button(root, text="GET",font=my_font,bg=button_color,fg=button_text_color,command=Get)
get_button.place(x=190,y=140)


root.mainloop()
