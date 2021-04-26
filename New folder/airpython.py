from tkinter import *
import os

master = Tk()

def open_timer():
    timer = "timer.py"
    os.system(timer)


def open_SimulationsSettings():
    sims = "SimulationSettings.py"
    os.system(sims)


def open_keyboard():
    os.system("keyboard.py")


def open_MySQL():
    os.system("MySQL.py")


def open_scope():
    os.system("scope.py")


def open_ScopeSettings():
    os.system("ScopeSettings.py")



b1 = Button(master, text="Timer", command= open_timer)
b1.grid(row=0, column=1)
b2 = Button(master, text="Simulation Settings", command= open_SimulationsSettings)
b2.grid(row=0, column=2) 
b3 = Button(master, text="Keyboard", command= open_keyboard)
b3.grid(row=2, column=1)
b4 = Button(master, text="MySQL", command= open_MySQL)
b4.grid(row=1, column=1)
b5 = Button(master, text="Scope", command= open_scope)
b5.grid(row=1, column=0)
b6 = Button(master, text="Scope Settings", command= open_ScopeSettings)
b6.grid(row=0, column=0) 



mainloop()
