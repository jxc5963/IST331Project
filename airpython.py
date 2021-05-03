from tkinter import *
import os
import time
from time import strftime
from functools import partial
#import mysql.connector
import json 
import googlemaps
from pprint import pprint
import urllib.request
import urllib.parse
import requests
from PIL import Image

master = Tk()
master.title("AirSimulation")

def open_timer():
    timer = "timer.py"

    root = Tk()
    root.title("Time")

    def time ():
        string = strftime("%H:%M:%S %p")
        label.config(text=string)
        label.after(1000,time)

    label = Label(root, font=("ds-digital", 80))
    label.pack(anchor = "center")
    time()

    print("Arrival Time: ", )
    print("Depature Time: ", )
    mainloop()
    #os.system(timer)


def open_SimulationsSettings():
    sims = "SimulationSettings.py"
    fenster = Tk()
    fenster.title("SimulationSettings")

    def switch():
        if b0["state"] == "normal":
            b0["state"] = "disabled"
            b2["text"] = "enable"
        elif b3["state"] == "normal":
            b0["state"] = "disabled"
            b2["text"] = "enable"
        else:
            b2["state"] = "normal"
            b2["text"] = "disable"

    #--Buttons
    b0 = Button(fenster, text="Settings", height=9, width=8)
    b0.grid(row=0, column=0)    

    b2 = Button(text="Timer", height=9, width=8)
    b2.grid(row=0, column=1)

    b3 = Button(fenster, text="Settings", height=19, width=12)
    b3.grid(row=0, column=2, rowspan=2) 

    b4 = Button(fenster, text="Settings", height=9, width=8)
    b4.grid(row=1, column=0) 

    b5 = Button(fenster, text="Settings", height=9, width=8)
    b5.grid(row=1, column=1)

    b6 = Button(fenster, text="Settings", height=9, width=22)
    b6.grid(row=2, column=1, columnspan=10)

    b7 = Button(fenster, text="Settings", height=9, width=8)
    b7.grid(row=2, column=0) 

    b8 = Button(fenster, text="Settings", height=9, width=8)
    b8.grid(row=0, column=1) 


    fenster.mainloop()
    os.system(sims)


def open_keyboard():
    Keyboard_App= Tk()
    Keyboard_App.title ("Keyboard")
    Keyboard_App ['bg']='powder blue'
    Keyboard_App.resizable(0,0)

    def select (value):
        if value =="Space":
            entry.insert(Keyboard_App.END,' ')

        elif value =="Space":
            entry.insert(Keyboard_App.END,'   ')
        else:
            entry.insert(Keyboard_App.END,value)

    label = Label(Keyboard_App, text="Keyboard", font=('arial',15,'bold'),
              bg='sky blue',fg="#000000").grid(row=0, columnspan = 40)
    entry = Text(Keyboard_App, width=118, font=('arial',8,'bold'))
    entry.grid(row=1, columnspan = 40)

    buttons=[
        'INTCNTL','TRKRPOS','TERMCNTL','HNDOFF','FLTDATA','MULTFUNC','F9','F10','F11','F12''F13','F14','TGT GEN''F6',
        '!','q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-',
        'Tab','a','s','d','f','g','h','j','k','l','[',']','4','5','6','+',
        'SHIFT','z','x','c','v','b','n','m',',','.','?','SHIFT','1','2','3','/',
        'Space'
    ]
    varRow=2
    varColumn=0



    for button in buttons:
        command = lambda x= button: select(x)
        if button != " Space":
            Keyboard_App.Button(Keyboard_App, text=button,width=5,padx =3,pady=3,bd=12,
                        font=('arial',12,'bold'),bg='sky blue',
                        activebackground='#ffffff',activeforeground='#000990',relief='raised',
                        command= command).grid(row=varRow,column=varColumn)
        if button == " Space":
            Keyboard_App.Button(Keyboard_App,text=button,width=300,padx =3,pady=3,bd=12,
                        font=('arial',12,'bold'),bg='sky blue',
                        activebackground='#ffffff',activeforeground='#000990',relief='raised',
                        command = command).grid(row=6,column=varColumn)

        varColumn+=1
        if varColumn > 15 and varRow ==2:
            varColumn =0
            varRow +=1 

        if varColumn > 15 and varRow ==3:
            varColumn =0
            varRow +=1 

    Keyboard_App.mainloop()
    os.system("keyboard.py")


def open_MySQL():
    os.system("MySQL.py")


def open_scope():
    url = 'https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ&center=-74.8871479081073,121.44776220633602&zoom=0&format=png&maptype=roadmap&style=element:geometry%7Ccolor:0x212121&style=element:labels.icon%7Cvisibility:off&style=element:labels.text.fill%7Ccolor:0x757575&style=element:labels.text.stroke%7Ccolor:0x212121&style=feature:administrative%7Celement:geometry%7Ccolor:0x757575&style=feature:administrative.country%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.locality%7Celement:labels.text.fill%7Ccolor:0xbdbdbd&style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:poi.park%7Celement:geometry%7Ccolor:0x181818&style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:poi.park%7Celement:labels.text.stroke%7Ccolor:0x1b1b1b&style=feature:road%7Celement:geometry.fill%7Ccolor:0x2c2c2c&style=feature:road%7Celement:labels.text.fill%7Ccolor:0x8a8a8a&style=feature:road.arterial%7Celement:geometry%7Ccolor:0x373737&style=feature:road.highway%7Celement:geometry%7Ccolor:0x3c3c3c&style=feature:road.highway.controlled_access%7Celement:geometry%7Ccolor:0x4e4e4e&style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:transit%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:water%7Celement:geometry%7Ccolor:0x000000&style=feature:water%7Celement:labels.text.fill%7Ccolor:0x3d3d3d&size=480x360'
    MAP_URL= "https://maps.googleapis.com/maps/api/staticmap?key=AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ&center=39.8729,75.2437=17&zoom=12&size=4000000x4000000&maptype=satellite&markers=color:black|label:|PhiladelphiaAirport"

    API_KEY= 'AIzaSyC91eORDd5nWBrVCsmUCK3e4cnpYn5d9DQ'
    city= 'Philadelphia'
    zoom= 14
    size= '500x500'

#URL2= MAP_URL + "center =" + city + "&zoom=" + str(zoom) + "size = &500x500&key="  + API_KEY
    response = requests.get(MAP_URL)

    with open ('Philadelphia.png','wb') as file:
        file.write(response.content)
        file.close()
        img= Image.open('Philadelphia.png')
        img.show()
        os.system("scope.py")


def open_ScopeSettings():
    fenster = Tk()
    fenster.title("ScopeSettings")
    def switch():
        if b0["state"] == "normal":
            b0["state"] = "disabled"
            b2["text"] = "enable"
        elif b3["state"] == "normal":
            b0["state"] = "disabled"
            b2["text"] = "ClickHere"
        else:
            b2["state"] = "normal"
            b2["text"] = "disable"

    #--Buttons
    b0 = Button(fenster, text="Settings", height=8, width=8)
    b0.grid(row=0, column=1)    

    b2 = Button(text="Settings", height=8, width=8)
    b2.grid(row=0, column=0)

    b3 = Button(fenster, text="Settings", height=8, width=8)
    b3.grid(row=0, column=2) 

    b4 = Button(fenster, text="Settings", height=8, width=8)
    b4.grid(row=0, column=3) 

    b5 = Button(fenster, text="Settings", height=8, width=8)
    b5.grid(row=0, column=4)

    b6 = Button(fenster, text="Settings", height=8, width=8)
    b6.grid(row=0, column=5)

    b7 = Button(fenster, text="Settings", height=8, width=8)
    b7.grid(row=0, column=6) 


    fenster.mainloop()
    os.system("ScopeSettings.py")



b2 = Button(master, text="Timer", command= open_timer)
b2.grid(row=0, column=1)
b1 = Button(master, text="Simulation Settings", command= open_SimulationsSettings)
b1.grid(row=0, column=2) 
b3 = Button(master, text="Keyboard", command= open_keyboard)
b3.grid(row=2, column=1)
b4 = Button(master, text="MySQL", command= open_MySQL)
b4.grid(row=1, column=1)
b5 = Button(master, text="Scope", command= open_scope)
b5.grid(row=1, column=0)
b6 = Button(master, text="Scope Settings", command= open_ScopeSettings)
b6.grid(row=0, column=0) 

master.mainloop()
