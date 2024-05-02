from tkinter import *

root = Tk()
root.title ('entry')
root.geometry('300x400')
root.resizable(width=False , height= False)

nameLable = Label(root , text = "please enter your name: ")
nameLable.place(x=8 , y=10)

nameInput = Entry(root)
nameInput.place(x=10 , y=40)

def get_name():
    print(nameInput.get())

btn = Button(root , text = 'Get name', command= lambda: get_name())
btn.place(x=10 , y=70)

root.mainloop()
