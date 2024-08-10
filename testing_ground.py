from tkinter import *
import testing_g1
import app_call


root = Tk()

root.title("Root Window")
root.geometry("512x256")

label1 = Label(root, text="This is the Root Window")
button = Button(root, text="Open Toplevel Window")
button.config(command=testing_g1.open_a_toplevel_window)

label1.pack()


button.place(x=110, y=50)
''



button1 = Button(root, text="Open Toplevel Windowb")
button1.config(command=app_call.open_b_toplevel_window)
button1.place(x=210, y=100)


root.mainloop()



