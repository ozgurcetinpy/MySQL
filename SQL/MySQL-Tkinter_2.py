from tkinter import *
import tkinter
import mysql.connector
from tkinter import END
from tkinter import messagebox
from mysql.connector import connect, connection



#DEFINE WINDOW

root = Tk()
root.title("Tkinter + MySQL")
root.geometry("430x650")
root.resizable(0,0)
root.iconbitmap("MySQL.ico")


#DEFINE FONTS AND COLORS
root_color = "#bed558"
my_font = ("Times New Roman",12)
button_color = "#f15946"
entry_color = "#034c3c"
input_frame_color = "#93032e"
output_frame_color = "#beb8eb"
label_color = "White"


root.config(bg=root_color)



#DEFINE FUNCTIONS
def Instert():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    if name == "" or surname == "" or phone == "":
        messagebox.showinfo("Insert Status","All fields are required")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password = "MySQLite.123", database = "tkinter"
        )
        cursor = connection.cursor()
        sql = "INSERT INTO customers (name,surname,phone) VALUES (%s,%s,%s)"
        values = (name,surname,phone)
        cursor.execute(sql,values)

        name_entry.delete(0,END)
        surname_entry.delete(0,END)
        phone_entry.delete(0,END)
        id_entry.delete(0,END)


        try:
            connection.commit()
        except mysql.connector.Error as err:
            messagebox.showinfo("ERROR FOUNDED","MySQL conneciton error... {}".format(err))
        finally:
            connection.close()
            messagebox.showinfo("CONNECTION CLOSED","DATA INSERTED\nCONECTION CLOSED")

def Delete():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    id = id_entry.get()
    if id == "":
        messagebox.showinfo("Delete Status","No ID Entered")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password = "MySQLite.123", database = "tkinter"
        )
        cursor = connection.cursor()
        sql = "DELETE FROM  customers where id = %s"
        value = (id,)
        cursor.execute(sql,value)

        name_entry.delete(0,END)
        surname_entry.delete(0,END)
        phone_entry.delete(0,END)
        id_entry.delete(0,END)

        try:
            connection.commit()
        except mysql.connector.Error as err:
            messagebox.showinfo("ERROR FOUNDED","MySQL conneciton error... {}".format(err))
        finally:
            connection.close()
            messagebox.showinfo("CONNECTION CLOSED","DATA DELETED\nCONECTION CLOSED")


def Update():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    id = id_entry.get()
    if id == "":
        messagebox.showinfo("Delete or Update Status","No ID Entered")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password = "MySQLite.123", database = "tkinter"
        )
        cursor = connection.cursor()
        if name != "":
            sql = "UPDATE customers SET name = %s  where id = %s"
            value = (name,id)
            cursor.execute(sql,value)
        if surname != "":
            sql = "UPDATE customers SET surname = %s  where id = %s"
            value = (surname,id)
            cursor.execute(sql,value)
        if phone != "":
            sql = "UPDATE customers SET phone = %s  where id = %s"
            value = (phone,id)
            cursor.execute(sql,value)

        name_entry.delete(0,END)
        surname_entry.delete(0,END)
        phone_entry.delete(0,END)
        id_entry.delete(0,END)

        try:
            connection.commit()
        except mysql.connector.Error as err:
            messagebox.showinfo("ERROR FOUNDED","MySQL conneciton error... {}".format(err))
        finally:
            connection.close()
            messagebox.showinfo("CONNECTION CLOSED","DATA UPDATED\nCONECTION CLOSED")


def Select():
    name = name_entry.get()
    surname = surname_entry.get()
    phone = phone_entry.get()
    id = id_entry.get()
    if id == "":
        messagebox.showinfo("DATA STATUS","No ID Entered")
    else:
        connection = mysql.connector.connect(
            host = "localhost", user = "root", password = "MySQLite.123", database = "tkinter"
        )
        cursor = connection.cursor()
        sql = "SELECT * from customers WHERE id = %s"
        value = (id,)
        cursor.execute(sql,value)

        liste = list(cursor.fetchone())
        for i in liste:
            insert_label = Label(listbox,text="ID={}\n".format(liste[0]),width=10,font=my_font,bg="White")
            insert_label.grid(row=0,column=0,padx=5,pady=5)
            insert_label = Label(listbox,text="Name={}\n".format(liste[1]),width=10,font=my_font,bg="White")
            insert_label.grid(row=1,column=0,pady=5,padx=5)
            insert_label = Label(listbox,text="Surname={}\n".format(liste[2]),width=10,font=my_font,bg="White")
            insert_label.grid(row=2,column=0,padx=5,pady=5)
            insert_label = Label(listbox,text="Phone Number={}\n".format(liste[3]),width=10,font=my_font,bg="White")
            insert_label.grid(row=3,column=0,pady=5,padx=5)
            
#DEFINE FRAMES
input_frame = LabelFrame(root,bg=input_frame_color,borderwidth=5)
input_frame.grid(row=0,column=0,padx=10,pady=10)

button_frame = Frame(root,bg=root_color,borderwidth=5)
button_frame.grid(row=1,column=0,padx=10,pady=(10,2))

output_frame = LabelFrame(root,bg=output_frame_color,borderwidth=5)
output_frame.grid(row=2,column=0,pady=10,padx=10)

#DEFINE LABELS
name_label = Label(input_frame,text="Enter Your Name",font=my_font,bg=input_frame_color,fg=label_color)
surname_label = Label(input_frame,text="Enter Your Surname",font=my_font,bg=input_frame_color,fg=label_color)
phone_label = Label(input_frame,text="Enter Your Phone Number",font=my_font,bg=input_frame_color,fg=label_color)
id_label = Label(input_frame,text="Enter ID You Want\n To Update Or Delete",font=my_font,bg=input_frame_color,fg=label_color)
name_label.grid(row=0,column=0,padx=(5,65),pady=5)
surname_label.grid(row=1,column=0,padx=(5,65),pady=5)
phone_label.grid(row=2,column=0,padx=(5,65),pady=5)
id_label.grid(row=3,column=0,padx=(5,65),pady=5)

#DEFINE ENTRIES
name_entry = Entry(input_frame,fg=entry_color,bg= root_color, font=my_font,width=15,borderwidth=5)
surname_entry = Entry(input_frame, fg=entry_color,bg = root_color, font=my_font,width=15,borderwidth=5)
phone_entry = Entry(input_frame,fg=entry_color,bg = root_color, font=my_font,width=15,borderwidth=5)
id_entry = Entry(input_frame,fg=entry_color,bg = root_color, font=my_font,width=5,borderwidth=5)
name_entry.grid(row=0,column=1,padx=15,pady=15)
surname_entry.grid(row=1,column=1,pady=15,padx=15)
phone_entry.grid(row=2,column=1,pady=15,padx=15)
id_entry.grid(row= 3,column=1,pady=15,padx=15)

#DEFINE BUTTONS
insert_button = Button(button_frame,text="Insert",bg=button_color,font=my_font,fg=label_color,width=8,borderwidth=3,command=Instert)
delete_button = Button(button_frame,text="Delete",bg=button_color,font=my_font,fg=label_color,width=8,borderwidth=3,command=Delete)
update_button = Button(button_frame,text="Update",bg=button_color,font=my_font,fg=label_color,width=8,borderwidth=3,command=Update,)
select_button = Button(button_frame,text="Show",bg=button_color,font=my_font,fg=label_color,width=8,borderwidth=3,command=Select)
insert_button.grid(row=0,column=0,padx=5,pady=10)
delete_button.grid(row=0,column=1,padx=5,pady=10)
update_button.grid(row=0,column=2,padx=5,pady=10)
select_button.grid(row=0,column=3,padx=5,pady=10)

#DEFINE LISTBOX
listbox = Listbox(output_frame,width=55,height=15,borderwidth=5)

listbox.grid(row=0,column=0,pady=(10,2),padx=5)

#DEFINE LOOP
root.mainloop()