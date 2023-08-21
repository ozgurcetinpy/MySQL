import mysql.connector
from tkinter import *
import RPi.GPIO as GPIO
import time
from datetime import datetime


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# def Baglan():
#     conneciton = mysql.connector.connect(
#             host = '127.0.0.1', user = 'root', password = 'raspberry', database = 'pi')
    

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

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
    

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)
        sql=""
        user_time = int(time_entry.get())
        if distance > 2 and distance < 400:
            print ("Mesafe:",distance - 0.5,"cm")
            conneciton = mysql.connector.connect(host = '127.0.0.1', user = 'root', password = 'raspberry', database = 'pi')
            cursor = conneciton.cursor()
            time_now=datetime.now()
            #print(time_now)
            now_dis=distance - 0.5            
            sql = (f"INSERT INTO range_data (date,data) VALUES ('{str(time_now)}',{now_dis})")
            
            print(sql)
            cursor.execute(sql)
            conneciton.commit()
            conneciton.close()
                   
        else:
            print ('Menzil asildi')

        time.sleep(user_time)

root = Tk()
root.title("Raspberry_pi")
time_entry = Entry(root)
ok_button = Button(root,text="OK",command=Fonk)
connect_button = Button(root,text = "connect",command = Baglan)
time_entry.grid(row=0,column=0)
ok_button.grid(row=1,column=0)
connect_button.grid(row=1,column = 1)

root.mainloop()


