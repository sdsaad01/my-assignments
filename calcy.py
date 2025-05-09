from tkinter import * 

Window = Tk()
Window.geometry("500x500")


e = Entry(Window , width=56 , borderwidth= 6)
e.place(x=5 , y=0)

def click(num):
    result = e.get()
    e.delete(0 , END)
    e.insert(0 , str(result) + str(num))

b = Button(Window , text="1" , width=8 , command= lambda:click(1))
b.place(x=20 , y=80)
b = Button(Window , text="2" , width=8 , command= lambda:click(2))
b.place(x=100 , y=80)
b = Button(Window , text="3" , width=8 , command= lambda:click(3))
b.place(x=180 , y=80)
b = Button(Window , text="4" , width=8 , command= lambda:click(4))
b.place(x=20 , y=120)
b = Button(Window , text="5" , width=8, command= lambda:click(5))
b.place(x=100 , y=120)
b = Button(Window , text="6" , width=8, command= lambda:click(6))
b.place(x=180 , y=120)
b = Button(Window , text="7" , width=8, command= lambda:click(7))
b.place(x=20 , y=160)
b = Button(Window , text="8" , width=8, command= lambda:click(8))
b.place(x=100 , y=160)
b = Button(Window , text="9" , width=8, command= lambda:click(9))
b.place(x=180 , y=160)
b = Button(Window , text="0" , width=8, command= lambda:click(0))
b.place(x=20 , y=200)


def add():
    n1 = e.get()
    global math 
    math = "addition"
    global i 
    i = int(n1)
    e.delete(0 , END)
b = Button(Window , text="+" , width=8 , command= add)
b.place(x=100 , y=200)

def sub():
    n1 = e.get()
    global math 
    math = "substraction"
    global i 
    i = int(n1)
    e.delete(0 , END)
b = Button(Window , text="-" , width=8 , command= sub)
b.place(x=180 , y=200)

def mult():
    n1 = e.get()
    global math 
    math = "multiply"
    global i 
    i = int(n1)
    e.delete(0 , END)
b = Button(Window , text="*" , width=8 , command= mult)
b.place(x=20 , y=245)

def div():
    n1 = e.get()
    global math 
    math = "division"
    global i 
    i = int(n1)
    e.delete(0 , END)
b = Button(Window , text="/" , width=8 , command=div)
b.place(x=100 , y=245)

def equal():
    n2 = e.get()
    e.delete(0 , END)
    if math =="addition":
      e.insert(0 , i + int(n2))
    elif math=="substraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0 , i * int(n2))
    elif math=="division":
        e.insert(0 , i / int(n2))



b = Button(Window , text="=" , width=8 , command= equal)
b.place(x=180 , y=245)

def clear():
    e.delete(0 , END)
b = Button(Window , text="clear" , width=8 , command= clear)
b.place(x=20 , y=280)


mainloop()
