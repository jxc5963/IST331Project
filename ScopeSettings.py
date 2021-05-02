from tkinter import *

fenster = Tk()
fenster.title("ScopeSettings")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b2["text"] = "enable"
    elif b3["state"] == "normal":
         b1["state"] = "disabled"
         b2["text"] = "ClickHere"
    else:
        b2["state"] = "normal"
        b2["text"] = "disable"

#--Buttons
b1 = Button(fenster, text="Settings", command=switch, height=8, width=8)
b1.grid(row=0, column=1)    

b2 = Button(text="disable", command=switch)
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