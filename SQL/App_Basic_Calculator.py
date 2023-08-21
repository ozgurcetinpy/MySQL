from tkinter import *
from tkinter import END
from tkinter import RIGHT
from tkinter import DISABLED, NORMAL


# Define Root
root = Tk()
root.title("Calculator")
# root.iconbitmap("calc.ico")
root.geometry("300x400")
root.resizable(0,0)

#Define Fonts and Colors
dark_green = "#93af22"
light_green = "#acc254"
white_green = "#edefe0"
button_font =  ("Arial",18)
display_font = ("Arial",30)

#Define Funcitons
def SubmitNumber(number):
    """ add a number or decimal to the display"""
    display.insert(END,number)  # Start at the end of the display and write the number which is clicked.
    #if decimal was pressed disable the decimal button so it ccan not be pressed twice
    if "." in display.get():    
        decimal_button.config(state=DISABLED)  

def Operate(operator):
    """ Store the first number of the expression and the operation to be used """
    global first_number
    global operation

    #Get the operator pressed and the current value of the display. This is the first number in the calculation
    operation = operator
    first_number = display.get() 
    #Delete the value (first_number) from entry Display 
    display.delete(0,END)

    #Disable all operator
    add_button.config(state=DISABLED)
    multiply_button.config(state=DISABLED)
    divide_button.config(state=DISABLED)
    subtract_button.config(state=DISABLED)
    exponent_button.config(state=DISABLED)
    inverse_button.config(state=DISABLED)
    square_button.config(state=DISABLED)
    #Return decimal button to normal
    decimal_button.config(state=NORMAL)

def Equal():
    """ Run the stored operation for two number"""
    if operation == "add":
        value = float(first_number) + float(display.get())
    elif operation == "subtract":
        value = float(first_number) - float(display.get())
    elif operation == "multiply":
        value = float(first_number) * float(display.get())
    elif operation == "divide":
        if display.get() == 0:
            value = "ERROR"
        else:
            value = float(first_number) / float(display.get())
    elif operation == "exponent":
        value = float(first_number) ** float(display.get())

    display.delete(0,END)
    display.insert(0,value)

    EnableButtons()

def EnableButtons():
    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)
    multiply_button.config(state=NORMAL)
    divide_button.config(state=NORMAL)
    subtract_button.config(state=NORMAL)
    exponent_button.config(state=NORMAL)
    inverse_button.config(state=NORMAL)
    square_button.config(state=NORMAL)
    
def Clear():
    #Clear the display
    display.delete(0,END)

    EnableButtons()

def Inverse():
    if display.get() == 0:
        value = "ERROR"
    else:
        value = 1/float(display.get())
    
    display.delete(0,END)
    display.insert(0,value)

def Square():
    value = float(display.get()) ** 2

    display.delete(0,END)
    display.insert(0,value)

def Negate():
    value = -1 *float(display.get())

    display.delete(0,END)
    display.insert(0,value)




#Define GUI Layout

#Define Frames
display_frame = LabelFrame(root)
button_frame = LabelFrame(root)
display_frame.pack(padx=2,pady=(5,20))
button_frame.pack(padx=2,pady=5)

#Layout for the Display Frame
display = Entry(display_frame,width=50,font=display_font,bg=white_green,borderwidth=5,justify=RIGHT)
display.pack(padx=5,pady=5)

#Layout for the Button Frame
clear_button = Button(button_frame,text= "Clear", font=button_font,bg=dark_green,command=Clear)
quit_button = Button(button_frame,text= "Quit", font=button_font,bg=dark_green,command=root.destroy)

inverse_button = Button(button_frame, text="1/x",font=button_font,bg=light_green,command=Inverse)   
square_button = Button(button_frame, text="x^2",font=button_font,bg=light_green,command=Square)
exponent_button = Button(button_frame, text="x^n",font=button_font,bg=light_green,command=lambda:Operate("exponent"))
divide_button = Button(button_frame, text=" / ",font=button_font,bg=light_green,command=lambda:Operate("divide"))
multiply_button = Button(button_frame, text="*",font=button_font,bg=light_green,command=lambda:Operate("multiply"))
subtract_button = Button(button_frame, text="-",font=button_font,bg=light_green,command=lambda:Operate("subtract"))
add_button = Button(button_frame, text="+",font=button_font,bg=light_green,command=lambda:Operate("add"))
equal_button = Button(button_frame, text="=",font=button_font,bg=dark_green,command=Equal)
decimal_button = Button(button_frame, text=".",font=button_font,bg="Black",fg="White",command=lambda:SubmitNumber("."))
negate_button = Button(button_frame, text="+/-",font=button_font,bg="Black",fg="White",command=Negate)

nine_button = Button(button_frame,text=9,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(9))
eight_button = Button(button_frame,text=8,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(8))
seven_button = Button(button_frame,text=7,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(7))
six_button = Button(button_frame,text=6,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(6))
five_button = Button(button_frame,text=5,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(5))
four_button = Button(button_frame,text=4,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(4))
three_button = Button(button_frame,text=3,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(3))
two_button = Button(button_frame,text=2,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(2))
one_button = Button(button_frame,text=1,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(1))
zero_button = Button(button_frame,text=0,font=button_font,bg="Black", fg="White",command=lambda:SubmitNumber(0))


#First Row
clear_button.grid(row=0,column=0,pady = 1,sticky="WE",columnspan=2)
quit_button.grid(row=0,column=2,pady = 1,sticky="WE",columnspan=2)
#Second Row
inverse_button.grid(row=1,column=0,pady=1,sticky="WE")
square_button.grid(row=1,column=1,pady=1,sticky="WE")
exponent_button.grid(row=1,column=2,pady=1,sticky="WE")
divide_button.grid(row=1,column=3,pady=1,sticky="WE")
#Third Row
seven_button.grid(row=2,column=0,pady=1,sticky="WE",ipadx=20)
eight_button.grid(row=2,column=1,pady=1,sticky="WE",ipadx=20)
nine_button.grid(row=2,column=2,pady=1,sticky="WE",ipadx=20)
multiply_button.grid(row=2,column=3,pady=1,sticky="WE",ipadx=20)
#Fourth Row
four_button.grid(row=3,column=0,pady=1,sticky="WE")
five_button.grid(row=3,column=1,pady=1,sticky="WE")
six_button.grid(row=3,column=2,pady=1,sticky="WE")
subtract_button.grid(row=3,column=3,pady=1,sticky="WE")
#Fifth Row
one_button.grid(row=4,column=0,pady=1,sticky="WE")
two_button.grid(row=4,column=1,pady=1,sticky="WE")
three_button.grid(row=4,column=2,pady=1,sticky="WE")
add_button.grid(row=4,column=3,pady=1,sticky="WE")
#Sixth Row
negate_button.grid(row=5,column=0,pady=1,sticky="WE")
zero_button.grid(row=5,column=1,pady=1,sticky="WE")
decimal_button.grid(row=5,column=2,pady=1,sticky="WE")
equal_button.grid(row=5,column=3,pady=1,sticky="WE")



#Define The Mainloop
root.mainloop()