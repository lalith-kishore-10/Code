
from tkinter import *
from tkinter import messagebox

Application = Tk()
Application.geometry("300x300")
Application.title("Login form")

def login():
    uname = ee.get()
    pwd = ee2.get()
    
    if (uname == pwd):
        messagebox.showinfo("Info","Both Username and Password cannot be same!")
    
    elif (uname == "" and pwd == ""):
        messagebox.showinfo("Info","Blank not allowed")

    else:
        messagebox.showwarning("WARNING","Incorrect username or password!")

def quit():
    Application.destroy()
    print('Thanks For using my application')

L = Label(Application, text = 'Applications from the DH corp. Pvt LTD')
ll = Label(Application)
l = Label(Application, text = 'Login Form')
el = Label(Application, text = 'Username : ')
ee = Entry(Application)
el2  = Label(Application, text = 'Password : ')
ee2 = Entry(Application, show =  '*')
b = Button(Application, text = 'Login', command = login)
b2 = Button(Application, text = 'Quit', command = quit)
c = Label(Application, text = '')

L.pack()
ll.pack()
l.pack()
el.pack()
ee.pack()
el2.pack()
ee2.pack()
b.pack()
c.pack()
b2.pack()

Application.mainloop()