from tkinter import*
from tkinter.ttk import*

from time import strftime

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