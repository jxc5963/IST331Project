import flightstrip 
import mysql.connector

db = mysql.connector.connect(user= "root", passwd= "alexweber99", host = "localhost", database = "testdatabase")

mycursor= db.cursor()
mycursor.execute("SELECT * FROM flightlists")
for x in mycursor:
    print (x)