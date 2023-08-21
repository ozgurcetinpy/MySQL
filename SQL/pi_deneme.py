import mysql.connector
from tkinter import *
import RPI.GPIO as GPIO
import time
import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def Fonk():

    TRIG = 23
    ECHO = 24

    print ('HC-SR04 mesafe sensoru')

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    while True:

        GPIO.output(TRIG, False)
        print ("Olculuyor...")
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        print (time.time())

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
    

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        sql=""
        if distance > 2 and distance < 400:
            print ("Mesafe:",distance - 0.5,"cm")
            user_time = time_entry.get()
            conneciton = mysql.connector.connect(
                host = "localhost", user = "root", password = "raspberry", database = "pi"
            )
            cursor = conneciton.cursor()
            sql = "INSERT INTO range_data (date,data) VALUES ("+datetime.now()+","+distance - 0.5+")"
            cursor.execute(sql)
            try:
                conneciton.commit()
            except mysql.connector.Error as Err:
                print("Hata : ",Err)    
        else:
            print ('Menzil asildi')

        time.sleep(user_time)

root = Tk()
root.title("Raspberry_pi")
time_entry = Entry(root)
ok_button = Button(root,text="OK")
time_entry.grid(row=0,column=0)
ok_button.grid(row=1,column=0)

root.mainloop()

