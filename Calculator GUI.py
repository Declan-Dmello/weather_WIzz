#12:01 pm to 17:07 pm
#10/08/2022
#AUTHOR = DC_THE_GREAT

from tkinter import *
import ctypes
root = Tk()
root.title("GUI CALCULATOR ")



#root.geometry("500x500")



e=Entry(root,width=50, bg= "#82EEFD" , fg ="black", borderwidth=4,relief=FLAT)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



#ALL THE BUTTONS
def button_a(number):
    #e.delete(0,END)
    cur = e.get()
    e.delete(0,END)
    e.insert(0,str(cur) + str(number))


def button_clear():
    e.delete(0 , END)


def button_add():
    first_no = e.get()
    global f_no
    global math
    math = "addition"
    f_no = int(first_no)
    e.delete(0,END)

def button_minus():
    first_no = e.get()
    global f_no
    global math
    math = "Subtraction"
    f_no = int(first_no)
    e.delete(0,END)

def button_multiply():
    first_no = e.get()
    global f_no
    global math
    math = "Multiplication"
    f_no = int(first_no)
    e.delete(0,END)

def button_divide():
    first_no = e.get()
    global f_no
    global math
    math = "Division"
    f_no = int(first_no)
    e.delete(0, END)

def button_equal():
    second_no = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_no + int(second_no))#CAN ALSO USE E.GETS()
    elif math == "Subtraction":
        e.insert(0,f_no - int(second_no))
    elif math == "Multiplication":
        e.insert(0,f_no * int(second_no))
    elif math == "Division":
        e.insert(0,f_no / int(second_no))




button_2 = Button(root, text="2", pady=20 , padx=35, command= lambda: button_a(2),bd ="3px",activebackground="yellow")
button_3 = Button(root, text="3", pady=20 , padx=35, command= lambda:button_a(3), bd="3px",activebackground="yellow")
button_4 = Button(root, text="4", pady=20 , padx=35, command= lambda:button_a(4), bd="3px",activebackground="yellow")
button_1 = Button(root, text="1", pady=20 , padx=35, command= lambda:button_a(1), bd="3px",activebackground="yellow")
button_5 = Button(root, text="5", pady=20 , padx=35, command= lambda:button_a(5), bd="3px",activebackground="yellow")
button_6 = Button(root, text="6", pady=20 , padx=35, command= lambda:button_a(6), bd="3px",activebackground="yellow")
button_7 = Button(root, text="7", pady=20 , padx=35, command=lambda: button_a(7), bd="3px",activebackground="yellow")
button_8 = Button(root, text="8", pady=20 , padx=35, command= lambda:button_a(8), bd="3px",activebackground="yellow")
button_9 = Button(root, text="9", pady=20 , padx=35, command= lambda:button_a(9), bd="3px",activebackground="yellow")
button_0 = Button(root, text="0", pady=20 , padx=35, command= lambda:button_a(0), bd="3px",activebackground="yellow")
button_add = Button(root, text="+", pady=20 ,padx=34, command= button_add, bd="3px",activebackground="yellow",bg="light blue")
button_minus = Button(root, text="-", pady=20 ,padx=34, command= button_minus, bd="3px",activebackground="yellow",bg="light blue")
button_multiply = Button(root, text="*", pady=20 ,padx=34, command= button_multiply, bd="3px",activebackground="yellow",bg="light blue")
button_divide = Button(root, text="/", pady=20 ,padx=34, command= button_divide, bd="3px",activebackground="yellow",bg="light blue")
button_equal = Button(root, text="=", pady=20 ,padx=34, command= button_equal, bd="3px",activebackground="yellow",bg="#0492C2")
button_clear = Button(root, text="C", pady=20 ,padx=34, command= button_clear, bd="3px",activebackground="yellow",bg="orange")







#display button
button_7.grid(row=1 ,column=0)
button_8.grid(row= 1,column=1)
button_9.grid(row= 1,column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row= 2,column=2)
button_multiply.grid(row=2, column=3)


button_1.grid(row= 3,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)
button_minus.grid(row=3, column=3)


button_clear.grid(row=4, column=0)
button_0.grid(row= 4,column=1)
button_add.grid(row= 4,column=2)
button_equal.grid(row= 4,column=3)




icon = PhotoImage(file= "pics/icons8-calculator-100.png")
root.iconphoto(True, icon)


taskbar_icon= 'RUI IS AN IDIOT' #input normal string for the
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(taskbar_icon)


root.mainloop()

