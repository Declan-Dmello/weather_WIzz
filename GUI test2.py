from tkinter import  *

root = Tk()
#root.geometry("600x400")
#Frames
"""



redFrame = tk.Frame(root, bg='light yellow')
redFrame.pack_propagate(0)
redFrame.pack(fill='both', side='left', expand='True')

blueFrame = tk.Frame(root, bg='sky blue')
blueFrame.pack_propagate(0)
blueFrame.pack(fill='both', side='right', expand='True')

greenFrame = tk.Frame(redFrame, width=100, height=100, bg='green')
greenFrame.pack_propagate(0)
greenFrame.pack(side='top', padx=0, pady=0, anchor='w')"""


#RADIO BUTTONS
#Buttons with Multiple answers like select the answer


#tkinter has different variables
#to check if someone clicked on it

#This functions keeps track to any changes to the variable
#Can also keep it as string with StrVar() if value is string
#r = IntVar()
pizza = StringVar()
#pizza.set("Pepperoni")
#r.set(2)#sets/selects value instead of getting

MODES = [("Pepperoni","Pepperoni"), #left is the text of the radio button , right is the text display after pressing the button
         ("Cheese","cheese"),
         ("Mushroom","Mushroom"),
         ("Onion","Onion")]
for text, mode in MODES:
    Radiobutton(root, text= text,variable=pizza, value=mode).pack(anchor=N)

def clicked(value):
    label1 = Label(frame1, text=value)
    label1.pack()
#prints the value which is printed
"""
Radiobutton(root, text="Option1", variable=pizza, value = 1, command=lambda: clicked(pizza.get()) ).pack()
Radiobutton(root, text="Option2", variable=pizza , value = 2, command=lambda: clicked(pizza.get()) ).pack()
"""
frame1 = Frame(root, bg='green')
frame1.pack(expand=True, fill=BOTH)
"""
label1 = Label(root,text =pizza.get() )
label1.pack()"""

#can also use the radio button as choice like choose one of the options and then click the button for something to happen !!
button1 = Button(frame1,text="Click me !!", command=lambda: clicked(pizza.get())).pack()


root.mainloop()


























"""
# sets the geometry of main
# root window
root.geometry("200x200")
#Showwarning makes an error noise with the popup
#showinfo , showwarning , showerror,askquestions, askokcancel,askyesno, askretrycancel,askyesnocancel
def popup():
    response = messagebox.askyesnocancel("Answer This!!", "IS TAIWAN AN INDEPENDENT COUNTRY?")
    #Label(root,text = response).pack()
    #some return "yes" and "no"
    if response == 1 :
        Label(root,text="RESPECT++").pack()
    elif response == 0 :
        Label(root,text="SOCIAL CREDIT++").pack()




Button1 = Button(root, text = "Popup", command = popup).pack()

"""





"""
# Create an instance of tkinter window


# Define the geometry of the window
root.geometry("700x500")

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("PngItem_4523738.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
"""

"""
root.geometry("600x400")

redFrame = tk.Frame(root, bg='light yellow')
redFrame.pack_propagate(0)
redFrame.pack(fill='both', side='left', expand='True')

blueFrame = tk.Frame(root, bg='sky blue')
blueFrame.pack_propagate(0)
blueFrame.pack(fill='both', side='right', expand='True')
"""
"""
greenFrame = tk.Frame(redFrame, width=100, height=100, bg='green')
greenFrame.pack_propagate(0)
greenFrame.pack(side='top', padx=0, pady=0, anchor='w')"""
#root.geometry("500x500")
"""
var = StringVar()

def show():
    label_1 = Label(root, text=var.get()).pack()


c = Checkbutton(root, text="dont check this!", variable=var, onvalue="PIZZA", offvalue="CHICKEN")
c.deselect()
c.pack()


btn = Button(root,text="Show Selection", command=show).pack()"""


"""
#ONLY PNG FILES
# can do different types of files including pdf file and stuff but only return location not opens it
def open():
    global img
    root.filename = filedialog.askopenfilename(initialdir="/pythonProject1/app test", title="Select a File",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    img = PhotoImage(file=root.filename)
    label1 = Label(image=img).pack()

btn = Button(root, text = "OPEN ", command=open).pack()"""






"""
# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="This is a new window").pack()


label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click

btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)
"""

# mainloop, runs infinitely

"""
# Create a photoimage object of the image in the path
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os


root.geometry("550x300+300+150")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()

btn = Button(root, text='open image', command=open_img).pack()

"""





"""root.geometry("1400x600")

label = Label(root,text="Main Window").pack()
def open():
    top = Toplevel()

    global img
    img = PhotoImage(file='download.png')
    label1 = Label(top,image=img)
    label1.pack()
    button2 = Button(top, text="EXIT", command = top.destroy).pack()
    #quit closes the entire program , destroy closes only the page

button = Button(root, text = "OPen second window", command= open).pack()
"""

"""
def show():
    label1 = Label(root, text=clicked.get()).pack()

options =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked,*options )
drop.pack()
btm = Button(root, text="Show selection", command=show).pack()"""
"""#create a database connection

conn = sqlite3.connect('address_book.db')

#creating cursor
c= conn.cursor()

#table
c.execute("" CREATE TABLE addresses(
            first_name text,
            last_name text ,
            address text , 
            city text,
            state text ,
            zipcode integer 
)

"")

conn.commit()

conn.close()"""




#pack on a different line not the same
"""vertical= Scale(root, from_ = 0 ,to=200)
vertical.pack()
horizontal = Scale (root, from_ = 0 , to= 200 , orient=HORIZONTAL)
horizontal.pack()


def slide():
    label1 = Label(root, text=horizontal.get()).pack()
    label2= Label(root, text=vertical.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


butn = Button(root, text="Click me", command= slide ).pack()
"""



"""
#creates another window
top = Toplevel()
label= Label(top, text = "LOLO").pack()"""




"""
import requests
import geocoder
from tkinter import *

root = Tk()

loc = "Cochin"

api1 = ""

def geocode():
    global search_bar
    global loc_name
    loc_name = search_bar.get()
    geo = geocoder.bing(loc_name, key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
    results = geo.json
    latitude1 = results['lat']
    longitude1 = results['lng']
    return [latitude1, longitude1]


# refresh the thing
def refresh():
    global label
    global loc
    global api1
    loc = Search_bar.get()
    api1 = api()
    label.configure(text=api1)


# gets the api
def api():
    global loc
    response1 = requests.get(
        "https://api.weatherapi.com/v1/current.json?key=7364c346c7444a62bb3121825223108&q={}".format(loc))
    dtWAPI = response1.json()
    location1 = dtWAPI["current"]["temp_c"]
    return location1


b1 = Button(root, text="btn", command=refresh)
b1.pack()
# binds the thing with the enter
# root.bind('<Return>', refresh)

# Shows the api result
label = Label(root, text=api())
label.pack()

# the search bar
Search_bar = Entry(root, width=50, bg="light blue", fg="red", borderwidth="5px", relief=FLAT)
Search_bar.pack()

# Search_bar.insert(0,"INPUT")
L1 = Label(root, text="Press")
L1.pack()

root.mainloop()"""
"""
global label1
global btn

def some():
    label1.config(text="This is new text!")
    root.config(bg="blue")
    btn.config(text="configured")


label1 = Label(root, text="This is my label", font=("Sans-serif",18))#use seperate bracket for font
label1.pack(pady=10)

btn = Button(root, text="Click me ", command=some)
btn.pack()
"""
"""
#img = PhotoImage(file='graph.png')
img2 = Image.open("download.png")
img2 = img2.resize((200,200))
test = ImageTk.PhotoImage(img2)
label1 = tkinter.Label(image=test)
label1.image = test

label1.pack()
#label1 = Label(root,image=img)
#label1.pack()
root.mainloop()"""



loc_name = input("Input a location : ")

geo = geocoder.bing(loc_name, key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
geo_results = geo.json
lat = geo_results['lat']
long = geo_results['lng']

"""

g = geocoder.bing([lat, long], method='reverse' , key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
go = g.json

location = go

print(lat)
print(long)
#location_list = location.split(",")
"""

response = requests.get("http://api.positionstack.com/v1/reverse?access_key=c71c8f5a32a2f4e942ec2facd5238ff9&query={},{}".format(lat, long))
dt = response.json()
a = dt["data"] [0]
l1 = a["locality"]
l2 = a["county"]
l3 = a["region"]
l4 = a["country"]
print(l1,l2,l3,l4)


import requests
lat = 15.5937
long = 73.8142
api_url = 'https://api.api-ninjas.com/v1/airquality?lat={}&lon={}'.format(lat,long)
response = requests.get(api_url, headers={'X-Api-Key': 'p7x7rZT5vz5vR/Bgrwc7hw==0xMYoim3COSTTrpe'})

dt = response.json()
print(dt["overall_aqi"])


"""from testing_g1 import *
from tkinter import *


def open_a_toplevel_window():
    toplevel_window = Toplevel(root9)
    toplevel_window.title('Focusing on Text Entery')
    toplevel_window.geometry('270x100')
    label = Label(toplevel_window, text='Enter Text Now')
    label.pack()
    text_entry = Text(toplevel_window, width=10, height=3)
    text_entry.focus_set()
    text_entry.pack()
    toplevel_window.attributes('-topmost', True)



#   toplevel_window.mainloop()

def open_b_toplevel_window():
    toplevel_window = Toplevel(root)
    toplevel_window.title('Focusing on Text Entery')
    toplevel_window.geometry('270x100')
    label = Label(toplevel_window, text='Enter Text Now')
    label.pack()
    text_entry = Text(toplevel_window, width=10, height=3)
    text_entry.focus_set()
    text_entry.pack()
    toplevel_window.attributes('-topmost', True)


#   toplevel_window.mainloop()

def open_c_toplevel_window():
    toplevel_window = Toplevel(root)
    toplevel_window.title('Focusing on Text Entery')
    toplevel_window.geometry('270x100')
    label = Label(toplevel_window, text='Enter Text Now')
    label.pack()
    text_entry = Text(toplevel_window, width=10, height=3)
    text_entry.focus_set()
    text_entry.pack()
    toplevel_window.attributes('-topmost', True)



root = Tk()

root.title("Root Window")
root.geometry("512x256")

label1 = Label(root, text="This is the Root Window")
button = Button(root, text="Open Toplevel Window")
button.config(command=open_a_toplevel_window)
button1 = Button(root, text="Open Toplevel Windowb")
button1.config(command=open_b_toplevel_window)
button2 = Button(root, text="Open Toplevel Windowc")
button2.config(command=open_c_toplevel_window)
label1.pack()
button2.place(x=50, y=75)
button1.place(x=210, y=100)
button.place(x=110, y=50)
#open_d_toplevel_window()


root.mainloop()"""




"""def open_a_toplevel_window():
    toplevel_window = Toplevel(root)
    toplevel_window.title('Focusing on Text Entery')
    toplevel_window.geometry('270x100')
    label = Label(toplevel_window, text='Enter Text Now')
    label.pack()
    text_entry = Text(toplevel_window, width=10, height=3)
    text_entry.focus_set()
    text_entry.pack()
    toplevel_window.attributes('-topmost', True)

mainloop()


"""

"""

from tkinter import *
import requests
root = Tk()
data = ""

def refresher():
    global data
    response = requests.get("http://worldtimeapi.org/api/timezone/America/Argentina/Salta")
    data = response.json()

    time1 = data['datetime'][12:19]
    text2.configure(text=time1)
    root.after(5000, refresher)
    # every second...
    date1 = data['datetime'][0:10]
    text1.configure(text=date1)



text1 = Label(root)
text1.pack()
text2 = Label(root)
text2.pack()

refresher()

root.mainloop()

"""