import mysql.connector
db = mysql.connector.connect(user= "root", passwd= "alexweber99", host = "localhost", database = "testdatabase")

mycursor= db.cursor()
#mycursor.execute ("ALTER TABLE flights ADD PrimaryKey int PRIMARY KEY AUTO_INCREMENT")
#mycursor.execute ("ALTER TABLE flights DROP PrimaryKey")
#mycursor.execute("INSERT INTO flights (FlightID, airline, origin, destination) VALUES (%s, %s, %s, %s)", ("AA1439", "American Airlines", "ACY", "PHL"))
#db.commit()
#mycursor.execute("DESCRIBE flights")
mycursor.execute("SELECT * FROM flights")
for x in mycursor:
    print (x)



