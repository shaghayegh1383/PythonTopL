from tkinter import *
import tkinter.messagebox
 
# ========================== settings ==================================
root = Tk()
root.title ('Calculator')
root.geometry ('500x400')
root.resizable (width=False , height= False)
color = 'gray'
root.configure(bg = color)
# ========================== Variables ==================================

num1 = StringVar()
num2 = StringVar()
res_value = StringVar()


# ========================== frames ==================================
top_first = Frame (root , width= 500 , height=100 , bg = color)
top_first.pack(side = TOP)

top_second = Frame (root , width= 500 , height=100 , bg = color)
top_second.pack(side = TOP)

top_third = Frame (root , width= 500 , height=100 , bg = color)
top_third.pack(side = TOP)

top_fourth = Frame (root , width= 500 , height=100 , bg = color)
top_fourth.pack(side = TOP)
# ==========================Functions ==================================
def errormsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'Something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('division zero error', 'Something went wrong')
        
        


def plus():
    try:
        value = float(num1.get()) + float (num2.get())
        res_value.set(value)
    except:
        errormsg('error')
        
def minus():
    try:
        value = float(num1.get()) - float (num2.get())
        res_value.set(value)
    except:
        errormsg('error')
        
def mul():
    try:
        value = float(num1.get()) * float (num2.get())
        res_value.set(value)
    except:
        errormsg('error')
        
def div():
    if num2.get == '0':
        errormsg('division zero error')
    try:
        value = float(num1.get()) / float (num2.get())
        res_value.set(value)
    except:
        errormsg('error')
        


# ========================== Buttons ==================================
btn_plus = Button (top_third , text= '+' , width= 15 , highlightbackground= color , command= lambda:plus())
btn_plus.pack (side= LEFT , padx= 4 , pady= 4)

btn_minus = Button (top_third , text= '-' , width= 15 , highlightbackground= color, command= lambda:minus())
btn_minus.pack (side= LEFT , padx= 4 , pady= 4)

btn_mul = Button (top_third , text= '*' , width= 15 , highlightbackground= color , command= lambda:mul())
btn_mul.pack (side= LEFT , padx= 4 , pady= 4)

btn_div = Button (top_third , text= '/' , width= 15, highlightbackground= color, command= lambda:div())
btn_div.pack (side= LEFT , padx= 4 , pady= 4)

# ========================== Entries and lables ==================================
lable_first_num = Label (top_first ,text = 'Input number 1 :', bg= color )
lable_first_num.pack (side= LEFT , padx= 10 , pady= 50)

first_num = Entry(top_first , highlightbackground= color , textvariable= num1)
first_num.pack (side=LEFT)

lable_second_num = Label (top_second ,text = 'Input number 2 :', bg= color )
lable_second_num.pack (side= LEFT , padx= 10 , pady= 50)

second_num = Entry(top_second , highlightbackground= color , textvariable= num2)
second_num.pack (side=LEFT)

res = Label (top_fourth ,text = 'Result :', bg= color )
res.pack (side= LEFT , padx=10  , pady= 50)

res_num = Entry(top_fourth , highlightbackground= color , textvariable= res_value)
res_num.pack (side=LEFT)




root.mainloop()