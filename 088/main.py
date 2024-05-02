from tkinter import *

root = Tk()
my_name = StringVar()

def print_name():
    my_name.set('Hi Shaghayegh')

root.title('button')
root.geometry('400x300')
root.resizable(width=False , height= False)  # اندازشو دیگه ثابت میزاره بمونه

btn = Button(root , text= "click me!" , command = lambda:print_name())
btn.place(x=10 , y=10)

Label = Label(root , textvariable = my_name)
Label.place( x=10 , y=30 )

root.mainloop()