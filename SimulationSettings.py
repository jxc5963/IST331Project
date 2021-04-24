from tkinter import *

fenster = Tk()
fenster.title("SimulationSettings")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    elif b3["state"] == "normal":
         b1["state"] = "disabled"
         b2["text"] = "enable"
    else:
        b1["state"] = "normal"
        b2["text"] = "disable"

#--Buttons
b1 = Button(fenster, text="Settings", height=8, width=8)
b1.grid(row=0, column=0)    

b2 = Button(text="disable", command=switch)
b2.grid(row=0, column=1)

b3 = Button(fenster, text="Settings", height=25, width=12)
b3.grid(row=0, column=2, rowspan=3) 

b4 = Button(fenster, text="Settings", height=8, width=8)
b4.grid(row=1, column=0) 

b5 = Button(fenster, text="Settings", height=8, width=8)
b5.grid(row=1, column=1)

b6 = Button(fenster, text="Settings", height=8, width=20)
b6.grid(row=2, column=1, columnspan=10)

b7 = Button(fenster, text="Settings", height=8, width=8)
b7.grid(row=2, column=0) 


fenster.mainloop()