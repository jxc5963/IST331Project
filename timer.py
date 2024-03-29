import tkinter as Tkinter 
from datetime import datetime
counter = 0
running = False
def counter_label(label): 
    def count(): 
        if running: 
            global counter 

            if counter==0:             
                display=" "
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display=string 
    
            label['text']=display
    
            
            label.after(900, count)  
            counter += 1
    
    count()      
    
def Start(label): 
    global running 
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    add['state']='normal'
    sub['state']='normal'

def Stop(): 
    global running 
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    add['state']='normal'
    sub['state']='normal'
    running = False

def Reset(label): 
    global counter 
    counter=0

    if running==False:       
        reset['state']='disabled'
        label['text']=' '

    else:                
        label['text']=' '

def AddTime(label):
    def add(): 
        if running==True: 
            global counter 

            if counter==0:             
                display=" "
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display=string 
    
            label['text']=display
    
            
            label.after(900, add)  
            counter += 5
    
    add()


def SubTime(label):
    def sub(): 
        if running==True: 
            global counter 

            if counter==0:             
                display=" "
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%M:%S")
                display=string 
    
            label['text']=display
    
            
            label.after(900, sub)  
            counter -= 5
    
    sub()
    
root = Tkinter.Tk() 
root.title("Stopwatch") 
    

root.minsize(width=250, height=70) 
label = Tkinter.Label(root, text=" ", fg="black", font="Verdana 30 bold") 
label.pack() 
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label)) 
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop) 
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
add = Tkinter.Button(f, text='Add',width=6, state='disabled', command=lambda:AddTime(label)) 
sub = Tkinter.Button(f, text='Subtract',width=6, state='disabled', command=lambda:SubTime(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left") 
stop.pack(side ="left") 
reset.pack(side="left") 

add.pack(side="left")
sub.pack(side="left")

root.mainloop()