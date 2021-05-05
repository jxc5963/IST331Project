import flightstrip 
import mysql.connector

db = mysql.connector.connect(user= "root", passwd= "alexweber99", host = "localhost", database = "flights")

mycursor= db.cursor()
mycursor.execute("SELECT * FROM flightlist")
for x in mycursor:
    print (x)