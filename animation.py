import json
import mysql.connector
#from pprint import pprint
#import urllib.request
#import urllib.parse
#import requests
#from PIL import Image
import tkinter  as tk 
from tkinter import * 

root = Tk()
root.title('Animations')

#with open ('Philadelphia.png','wb') as file:
#     file.write(response.content)
#    file.close()
#    img= Image.open('Philadelphia.png')
#    img.show()

my_connect = mysql.connector.connect(
host="localhost",
user="root", 
passwd="alexweber99",
database="testdatabase"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM flights WHERE (FlighID = JBU4417)")
i=0 
for flights in my_conn: 
    for j in range(len(flights)):
        c = Canvas(root, width = 200, height = 100)
        c.pack()
        ball = c.create_oval(0, 15, 25, 50)
        for i in range(25):
            c.move(ball, 6, 0)
            root.after(40)


my_connect = mysql.connector.connect(
host="localhost",
user="root", 
passwd="alexweber99",
database="testdatabase"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM flights WHERE (FlighID = DAL8577)")
i=0 
for flights in my_conn: 
    for j in range(len(flights)):
        c1 = Canvas(root, width = 200, height = 100)
        c1.pack()
        ball = c1.create_oval(0, 15, 25, 50)
        for i in range(25):
            c1.move(ball, 6, 0)
            root.after(40)


my_connect = mysql.connector.connect(
host="localhost",
user="root", 
passwd="alexweber99",
database="testdatabase"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM flights WHERE (FlighID = AAL1234)")
i=0 
for flights in my_conn: 
    for j in range(len(flights)):
        c2 = Canvas(root, width = 200, height = 100)
        c2.pack()
        ball = c2.create_oval(0, 15, 25, 50)
        for i in range(25):
            c2.move(ball, 6, 0)
            root.after(40)

root.mainloop()
