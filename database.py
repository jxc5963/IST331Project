import mysql.connector
db = mysql.connector.connect(user= "root", passwd= "alexweber99", host = "localhost", database = "testdatabase")

mycursor= db.cursor()
#mycursor.execute("INSERT INTO flights (FlightID, airline, origin, destination) VALUES (%s, %s, %s, %s)", ("DA4564", "Delta", "JFK", "PHL"))

mycursor.execute("DESCRIBE flights")
mycursor.execute("SELECT * FROM flights")
#for x in mycursor:
    #print (x)



