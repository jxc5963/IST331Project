import tkinter as tk
from tkinter import ttk

key = tk.Tk()  # key window name
key.title('Keyboard')  # title Name

exp = " "  

def press(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)


def clear():
    global exp
    exp = " "
    equation.set(exp)

def action():
  exp = " Next Line : "
  equation.set(exp)

def Tab():
  exp = " TAB : "
  equation.set(exp)

# Size window size
key.geometry('5000x1000')         # normal size
key.maxsize(width=1150, height=400)      # maximum size
key.minsize(width= 1150 , height = 400)     # minimum size
# end window size

key.configure(bg = 'grey')    #  add background color

# entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly',textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)
# end entry box

# add all button line wise 

# First Line Button

clear1 = ttk.Button(key,text = 'Clear', width = 6, command =clear)
clear1.grid(row = 1 ,column = 0, ipadx = 6 , ipady = 10)

Back_Space = ttk.Button(key,text = 'Back Space' , width = 6, command = lambda : press('BACK SPACE'))
Back_Space.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

E = ttk.Button(key,text = 'Space', width = 6, command = lambda : press(' '))
E.grid(row = 1 , columnspan = 15, ipadx = 226 , ipady = 10)
#E.configure(bg = 'yellow') 

R = ttk.Button(key,text = 'Enter' , width = 6, command = action)
R.grid(row = 1 , column = 9, ipadx = 6, ipady = 10)

T = ttk.Button(key,text = 'INT CNTL' , width = 6, command = lambda : press('INT CNTL'))
T.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

Ye = ttk.Button(key,text = 'TRK RPOS' , width = 6, command = lambda : press('TRK RPOS'))
Ye.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

U = ttk.Button(key,text = 'TRK SUSP' , width = 6, command = lambda : press('TRK SUSP'))
U.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

I = ttk.Button(key,text = 'TERM CNTL' , width = 6, command = lambda : press('TERM CNTL'))
I.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)

O = ttk.Button(key,text = 'HND OFF' , width = 6, command = lambda : press('HND OFF'))
O.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)

P = ttk.Button(key,text = 'FLT DATA' , width = 6, command = lambda : press('FLT DATA'))
P.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)

cur = ttk.Button(key,text = 'MULT FUNC' , width = 6, command = lambda : press('MULTFUNC'))
cur.grid(row = 2 , column = 6 , ipadx = 6 , ipady = 10)

cur_c = ttk.Button(key,text = 'f8' , width = 6, command = lambda : press('f8'))
cur_c.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)

Delta = ttk.Button(key,text = '∆' , width = 6, command = lambda : press('∆'))
Delta.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)


clear = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
clear.grid(row = 2, column = 9, ipadx = 6 , ipady = 10)

# Third Line Button



F9= ttk.Button(key,text = 'F9' , width = 6, command = lambda : press('F9'))
F9.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)



F10= ttk.Button(key,text = 'F10' , width = 6, command = lambda : press('F10'))
F10.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)

F11 = ttk.Button(key,text = 'F11' , width = 6, command = lambda : press('F11'))
F11.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)

F12 = ttk.Button(key,text = 'F12' , width = 6, command = lambda : press('F12'))
F12.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)


F13 = ttk.Button(key,text = 'F13' , width = 6, command = lambda : press('F13'))
F13.grid(row = 3 , column = 4, ipadx = 6 , ipady = 10)


F14 = ttk.Button(key,text = 'F14' , width = 6, command = lambda : press('F14'))
F14.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)


Tgt_Gen = ttk.Button(key,text = 'TGT GEN' , width = 6, command = lambda : press('TGT GEN'))
Tgt_Gen.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)

F16 = ttk.Button(key,text = 'F16' , width = 6, command = lambda : press('F16'))
F16.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)


IFR= ttk.Button(key,text = 'IFR +' , width = 6, command = lambda : press('IFR +'))
IFR.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)

VFR = ttk.Button(key,text = 'vfr /' , width = 6, command = lambda : press('vfr /'))
VFR.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)

#new line 4
A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)


B = ttk.Button(key,text = 'B' , width = 6, command = lambda : press('B'))
B.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)


C = ttk.Button(key,text = 'C' , width = 6, command = lambda: press ('C'))
C.grid(row = 4 , column = 2, ipadx = 6 , ipady = 10)


D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 4 , column = 3, ipadx = 6 , ipady = 10)


E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 4 , column = 4, ipadx = 6 , ipady = 10)


F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 4 , column = 5, ipadx = 6 , ipady = 10)


G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 4 , column = 6, ipadx = 6 , ipady = 10)

One = ttk.Button(key, text= '1' , width = 6 , command = lambda : press('1'))
One.grid(row = 4 , column = 7 , ipadx = 6 ,ipady = 10)


Two = ttk.Button(key,text = '2' , width = 6, command = lambda : press('2'))
Two.grid(row = 4 , column = 8, ipadx = 6 , ipady = 10)

Three = ttk.Button(key,text = '3' , width = 6, command = lambda : press('3'))
Three.grid(row = 4 , column = 9, ipadx = 6 , ipady = 10)

#new line

H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 5 , column = 0, ipadx = 6 , ipady = 10)


I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 5 , column = 1, ipadx = 6 , ipady = 10)


J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 5, column = 2, ipadx = 6 , ipady = 10)


K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 5 , column = 3, ipadx = 6 , ipady = 10)


L= ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 5 , column = 4, ipadx = 6 , ipady = 10)


M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 5 , column = 5, ipadx = 6 , ipady = 10)

N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 5 , column = 6, ipadx = 6 , ipady = 10)

Four = ttk.Button(key,text = '4' , width = 6, command = lambda : press('4'))
Four.grid(row = 5 , column = 7, ipadx = 6 , ipady = 10)

Five = ttk.Button(key,text = '5' , width = 6, command = lambda : press('5'))
Five.grid(row = 5 , column = 8, ipadx = 6 , ipady = 10)


Six = ttk.Button(key,text = '6' , width = 6, command = lambda : press('6'))
Six.grid(row = 5 , column = 9, ipadx = 6 , ipady = 10)

#new line

V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 6 , column = 0, ipadx = 6 , ipady = 10)

W1 = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
W1.grid(row = 6 , column = 3, ipadx = 6 , ipady = 10)


X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 6 , column = 2 , ipadx = 6 , ipady = 10)

Y = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
Y.grid(row = 6 , columns = 3 , ipadx = 6 , ipady = 10)

Z= ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 6 , column = 4 , ipadx = 6 , ipady = 10)

Aster = ttk.Button(key,text = '*' , width = 6, command = lambda : press('*'))
Aster.grid(row = 6 , column = 5, ipadx = 6 , ipady = 10)

Empt = ttk.Button(key,text = '' , width = 6, command = lambda : press(''))
Empt.grid(row = 6 , column = 6 , ipadx = 6 , ipady = 10)


Empt1 = ttk.Button(key,text = '' , width = 6, command = lambda : press(''))
Empt1.grid(row = 6 , column = 7 , ipadx = 6 , ipady = 10)

Zero = ttk.Button(key,text = '0' , width = 6, command = lambda : press('0'))
Zero.grid(row = 6 , column = 8 , ipadx = 6 , ipady = 10)

Empt2 = ttk.Button(key,text = '' , width = 6, command = lambda : press(''))
Empt2.grid(row = 6 , column = 9 , ipadx = 6 , ipady = 10)



key.mainloop()  