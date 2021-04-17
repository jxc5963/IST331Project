from functools import partial
from tkinter import *
import tkinter

Keyboard_App= tkinter.Tk()
Keyboard_App.title ("Keyboard")
Keyboard_App ['bg']='sky blue'
Keyboard_App.resizable(0,0)

def select (value):
    if value =="Space":
        entry.insert(tkinter.END,' ')

    elif value =="Space":
        entry.insert(tkinter.END,'   ')
    else:
        entry.insert(tkinter.END,value)

label = Label(Keyboard_App, text="Keyboard", font=('arial',15,'bold'),
              bg='sky blue',fg="#000000").grid(row=0, columnspan = 40)
entry = Text(Keyboard_App, width=120, font=('arial',8,'bold'))
entry.grid(row=1, columnspan = 30)

buttons=[
    '!','q','w','e','r','t','y','u','i','o','p','<-','7','8','9','-',
    'Tab','a','s','d','f','g','h','j','k','l','[',']','4','5','6','+',
    'SHIFT','z','x','c','v','b','n','m',',','.','?','SHIFT','1','2','3','/',
    'Space'
]
varRow=2
varColumn=0



for button in buttons:
    command = lambda x= button: select(x)
    if button != " Space":
        tkinter.Button(Keyboard_App, text=button,width=5,padx =3,pady=3,bd=12,
                        font=('arial',12,'bold'),bg='sky blue',
                        activebackground='#ffffff',activeforeground='#000990',relief='raised',
                        command= command).grid(row=varRow,column=varColumn)
    if button == " Space":
        tkinter.Button(Keyboard_App,text=button,width=118,padx =3,pady=3,bd=12,
                        font=('arial',12,'bold'),bg='sky blue',
                        activebackground='#ffffff',activeforeground='#000990',relief='raised',
                        command = command).grid(row=6,column=varColumn)

    varColumn+=1
    if varColumn > 15 and varRow ==2:
        varColumn =0
        varRow +=1 

    if varColumn > 15 and varRow ==3:
        varColumn =0
        varRow +=1 

Keyboard_App.mainloop()

