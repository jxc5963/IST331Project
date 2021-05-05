import flightstrip 
import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="alexweber99",
  database="testdatabase"
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM flights limit 0,10")
i=0 
for flights in my_conn: 
    for j in range(len(flights)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, flights[j])
    i=i+1
my_w.mainloop()


#with open ("Flights.json",'r') as f:
    #json_file = json.load(f)
    

#class Table:
      
   # def __init__(self,root):
          
        # code for creating table
        #for i in range(total_rows):
            #for j in range(total_columns):
                  
                #self.e = Entry(root, width=20, fg='blue',
                 #              font=('Arial',16,'bold'))
                  
                #self.e.grid(row=i, column=j)
                #self.e.insert(END, lst[i][j])
  

# take the dat
#lst = [("flightId", "DA6789",
        #"aircraftType", "C172",)]

   
# find total number of rows and
# columns in list
#total_rows = len(lst)
#total_columns = len(lst[0])
   
# create root window
#root = Tk()
#t = Table(root)
#root.mainloop()


#for x in mycursor:
    #print (x)