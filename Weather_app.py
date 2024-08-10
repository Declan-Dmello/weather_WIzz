# AUTHOR : DCTHEGREAT A.K.A DECLAN DMELLO
# STARTED ON 10/08/2022
# TIME SPENT :103.45+3+1+1+4+1.30+2+7+0.45+6+3+10+1

# learning and research: 56.30+1
#ending it on 27-08-2022 to study for exams, might contiue it
#Started it back on 02-12-2022
from tkinter import *
import tkinter.font as tkFont
import tkinter as tk


from extra_info import extra_in
from extremes import extreme
from Current_Weather import *
from Forecast import forecast
from Weather_records import weather_rec
import ctypes


# if can import files from different files like inheritance or class
# can also add updated
# CREATING THE WINDOW AND FIXING ITS SIZE
#use pixel art gifs if time permits
#seperate file for API
#Arrangle Api properly and neatly
#make graph for wind speed
#give detailed comments of everything
#check api call limit before showing live
#might make a seperate file for the API data along with initialization of excess variables
#after finishing , make some changes like modern button and stuff
#change the font to something good
root = Tk()

root.geometry("1200x700")


frame = tk.Frame(root, width=1280, height=700, background='#306EFF')
frame.place(x =310 , y =0)

Frame(root, height=700, width=310, background="white").place(x=0,y=0)
# THE TITLE AND CENTERING THE TITLE
blank_space = " "
root.title(50 * blank_space + "WEATHER WIZZ")

font1 = tkFont.Font(family="Comic Sans MS", size=22,weight="bold")

# The search bar
Label(root, text=" WEATHER   WIZ",background="white", foreground='#306EFF', font=font1).place(x=20, y = 50)

main_image_list= ["pixel/clock-solid(1).png","pixel/sun(1).png","pixel/130-1307955_warning-sign-attention-caution-danger-symbol-black-box(1)-removebg-preview.png","pixel/icone-de-nuage-noir(1).png","pixel/196-1965401_transparent-books-vector-png-open-black-book-png(1).png"]


canvas_main1= Canvas(root, height=40, width=40, background="white", highlightthickness=0)
canvas_main1.place(x=20, y=175)
img_main1 = PhotoImage(file=main_image_list[0])
canvas_main1.create_image(20, 20, image=img_main1)

canvas_main2= Canvas(root, height=40, width=40, background="white", highlightthickness=0)
canvas_main2.place(x=20, y=260)
img_main2 = PhotoImage(file=main_image_list[1])
canvas_main2.create_image(20, 20, image=img_main2)

canvas_main3= Canvas(root, height=40, width=40, background="white", highlightthickness=0)
canvas_main3.place(x=20, y=345)
img_main3 = PhotoImage(file=main_image_list[3])
canvas_main3.create_image(20, 20, image=img_main3)

canvas_main4= Canvas(root, height=40, width=40, background="white", highlightthickness=0)
canvas_main4.place(x=20, y=430)
img_main4 = PhotoImage(file=main_image_list[2])
canvas_main4.create_image(20, 20, image=img_main4)

canvas_main5= Canvas(root, height=40, width=40, background="white", highlightthickness=0)
canvas_main5.place(x=20, y=515)
img_main5 = PhotoImage(file=main_image_list[4])
canvas_main5.create_image(20, 20, image=img_main5)


img_main_anchor = Image.open("pixel/cartoon-tv-weather-forecast-concept-vector-21106600-removebg-preview.png")
resize_anchor = img_main_anchor.resize((300, 250), Image.ANTIALIAS)
# draw image object
#I1 = ImageDraw.Draw(resize_anchor)
new_resized_CW = ImageTk.PhotoImage(resize_anchor)
label_image_main_anchor = Label(root, image=new_resized_CW, borderwidth=0).place(x=670,y=130)














def submit():
    c_w(search_bar.get())

def submit2():
    forecast(search_bar.get())

def submit3():
    extra_in(search_bar.get())


search_bar = Entry(root, width=85, bg="white", fg="#6D7B8D", borderwidth="5px", relief=FLAT)
search_bar.place(x=530, y = 65)
search_bar.insert(0,"Search on Weather Wiz")


font2 = tkFont.Font(family="Helvetica", size=8, weight = "bold")
font3 = tkFont.Font(family="Constantia", size=12, weight = "bold")
font4 = tkFont.Font(family="Comic Sans MS", size=20, weight = "bold")

#cambria
#OCR A Std
#Courier New
#Comic Sans MS
#Constantia
#Euphemia
#Gill Sans MT


Label(root,text="Welcome to Weather Wiz!", background='#306EFF', foreground="white",font=font4).place(x=600,y=470)

Label(root,text=" Get the most accurate and up-to-date weather information for your location \n and beyond. Stay ahead of the forecast with  daily weather predictions.\n Whether you're planning a road trip, a day at the beach,  or simply need to know \n if you should bring an umbrella, our app has you covered."
      , background='#306EFF', foreground="white",font=font2).place(x=580,y=530)



submit_button = Button(root,text="CURRENT   WEATHER",font=font3,background="white", command=submit, relief=FLAT)
submit_button.place(x=80, y=180)

submit_button2 = Button(root,text="WEATHER    FORECAST",font=font3,background="white", command=submit2, relief=FLAT)
submit_button2.place(x=80, y=265)

#435
submit_button3 = Button(root,text="AUXILIARY    WEATHER",font=font3,background="white", command=submit3, relief=FLAT)
submit_button3.place(x=80, y=350)

submit_button1 = Button(root,text="EXTREME    WEATHER",font=font3,background="white", command=extreme, relief=FLAT)
submit_button1.place(x=80, y=435)


button3 = Button(root, text="WEATHER    RECORDS",font=font3,background="white", command=weather_rec, relief=FLAT )
button3.place(x=80, y=520)




# THE TOP ICON OF THE APP
icon = PhotoImage(file='../PngItem_4523738.png')  # use low size image like 420 * 420 or something like that
root.iconphoto(True, icon)

# THE TASKBAR ICON
taskbar_icon = 'RUI IS AN IDIOT'  # random string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(taskbar_icon)

# THE MAIN LOOP
root.mainloop()
