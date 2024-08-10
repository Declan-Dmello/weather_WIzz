from tkinter import *
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
from re import search
import datetime
import calendar
from data3 import *



def fubc():
    root1 = Toplevel()
    root1.attributes("-fullscreen", True)

    temp = 2
    datetime1 = "2022-10-02 21:35"
    date1 = datetime1[0:10]
    hour = 10

    temp_min = 11
    temp_max = 45

    locality = "locality"
    county = "county"
    region = "region"
    country = "Country"

    description = "Rain"

    if locality is None:
        location_1 = county
    else:
        location_1 = locality + "," + county

    location_2 = region + "," + country

    """dtBIT = apiBIT
    description = dtBIT["data"][0]["weather"]["description"]"""

    # png list
    img_list = ['pixel/rain_day.jpg', 'pixel/day_clouds.png', 'pixel/night_rain.png', 'pixel/night_clouds.png',

                'pixel/night_clear.jpg', 'pixel/day_clear.jpg']

    # creating variables
    rain = "rain"
    cloud = "cloud"
    day = 6 <= hour < 20
    night = 20 <= hour <= 23 or 0 <= hour < 6
    Labelframe_image = ""

    if night:
        if search(rain, description):
            Labelframe_image = img_list[2]  # night rain
        elif search(cloud, description):
            Labelframe_image = img_list[3]  # night clouds
        else:
            Labelframe_image = img_list[4]  # night clear
    elif day:
        if search(rain, description):
            Labelframe_image = img_list[0]  # day rain
        elif search(cloud, description):
            Labelframe_image = img_list[1]  # day clouds
        else:
            Labelframe_image = img_list[5]  # day clear

    # Finding month name and weekday
    year, month, day = map(int, date1.split("-"))
    my_date = datetime.date(year, month, day)

    # True day, month , year
    True_weekday = calendar.day_name[my_date.weekday()]
    True_month = calendar.month_name[my_date.month]
    True_day = datetime1[8:11]

    # Joining the data together
    DT = str(True_month[0:3]) + " " + str(True_day) + "," + str(True_weekday[0:3])
    temp_min_max = str(temp_min) + "°C/" + str(temp_max) + "°C"

    # Opening a image from the List
    img = Image.open(Labelframe_image)
    rz_img = img.resize((600, 400), Image.ANTIALIAS)
    # draw image object
    I1 = ImageDraw.Draw(rz_img)

    # The font
    txt1 = 'arial.ttf'
    txt = 'vera.ttf'

    # add text to image
    font = ImageFont.truetype(txt1, 60)
    font1 = ImageFont.truetype(txt, 25)
    font2 = ImageFont.truetype(txt, 18)

    # Creating a LabelFrame
    LF_CW = LabelFrame(root1, highlightbackground="black", highlightthickness=2, relief=FLAT)
    LF_CW.place(x=2, y=100)

    # Modifying and displaying the ext data
    I1.text((25, 260), str(temp), font=font, fill="#FFFFFF")
    I1.text((150, 270), "°C", font=font2, fill="#FFFFFF")
    I1.text((25, 330), str(DT), font=font2, fill="#FFFFFF")
    I1.text((150, 288), str(description), font=font1, fill="#FFFFFF")
    I1.text((150, 330), str(temp_min_max), font=font2, fill="#FFFFFF")
    I1.text((25, 10), str(location_1), font=font2, fill="#FF6700")
    I1.text((25, 30), str(location_2), font=font2, fill="#FF6700")

    img2 = ImageTk.PhotoImage(rz_img)
    Label(LF_CW, image=img2).grid(row=5, column=5)

    # AQI WIDGET
    """dtAN = apiAN
    AQI = dtAN["overall_aqi"]"""

    AQI = 55

    bg_colour = ""
    colours = ["#43C6DB", "#6CBB3C", "#FFD700", "#FF6700", "#3D0C02", "#C11B17"]

    AQI_Health_Advice = ""
    title_font = ""

    AQI_description = ""
    AQI_fg_colour = ""
    AQI_description_fg = ""
    AQI_HA_fg = ""
    AQI_x = 0
    AQI_description_x = 0
    AQI_HA_x = 0

    if AQI < 33:
        bg_colour = colours[0]
        AQI_fg_colour = "gold"
        AQI_description = "Excellent"
        AQI_description_fg = "#1F45FC"
        AQI_Health_Advice = AQI_HA1
        AQI_HA_fg = "#FFE6E8"
        title_font = "black"
        AQI_x = 139
        AQI_description_x = 105
        AQI_HA_x = 80

    elif 33 < AQI <= 66:
        bg_colour = colours[1]
        AQI_fg_colour = "gold"
        AQI_description = "Good"
        AQI_description_fg = "#1F45FC"
        AQI_Health_Advice = AQI_HA2
        AQI_HA_fg = "#FFE6E8"
        title_font = "black"
        AQI_x = 139
        AQI_description_x = 135
        AQI_HA_x = 40

    elif 66 < AQI <= 99:
        bg_colour = colours[2]
        AQI_fg_colour = "#56A5EC"
        AQI_description = "Moderate"
        AQI_description_fg = "#FD1C03"
        AQI_Health_Advice = AQI_HA3
        AQI_HA_fg = "black"
        title_font = "black"
        AQI_x = 139
        AQI_description_x = 105
        AQI_HA_x = 30

    elif 99 < AQI <= 149:
        bg_colour = colours[3]
        AQI_fg_colour = "gold"
        AQI_description = "Poor"
        AQI_description_fg = "#1E90FF"
        AQI_Health_Advice = AQI_HA4
        AQI_HA_fg = "#FFE6E8"
        title_font = "black"

        AQI_x = 105
        AQI_description_x = 136
        AQI_HA_x = 15

    elif 149 < AQI <= 200:
        bg_colour = colours[4]
        AQI_fg_colour = "gold"
        AQI_description = "Very Poor"
        AQI_description_fg = "red"
        AQI_Health_Advice = AQI_HA5
        AQI_HA_fg = "#FFE6E8"
        title_font = "white"
        AQI_x = 105
        AQI_description_x = 95
        AQI_HA_x = 20

    elif AQI > 200:
        bg_colour = colours[5]
        AQI_fg_colour = "gold"
        AQI_description = "Hazardous"
        AQI_description_fg = "#77DD77"
        AQI_Health_Advice = AQI_HA6
        AQI_HA_fg = "#FFE6E8"
        title_font = "white"

        AQI_x = 115
        AQI_description_x = 90
        AQI_HA_x = 70

    LF_AQI = LabelFrame(root1, bg=bg_colour, bd="5px", relief=FLAT,
                        highlightbackground="#2916F5", highlightthickness=2, height=410, width=400)  # border thickness
    LF_AQI.place(x=880, y=100)  # 880

    # LABELS
    Label(LF_AQI, text="AIR   QUALITY   INDEX", bg=bg_colour, font=("bahnschrift", 20), fg=title_font).place(x=55, y=50)

    Label(LF_AQI, text=AQI, bg=bg_colour, font=("Sans-serif", 60), fg=AQI_fg_colour).place(x=AQI_x, y=120)

    Label(LF_AQI, text=AQI_description, bg=bg_colour, font=("bahnschrift", 30), fg=AQI_description_fg).place(
        x=AQI_description_x, y=220)

    Label(LF_AQI, text=AQI_Health_Advice, bg=bg_colour, font=8, fg=AQI_HA_fg).place(x=AQI_HA_x, y=280)

    # TITLE BAR
    LF_Title = LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="black", highlightthickness=2, height=100,
                          width=1278)
    LF_Title.place(x=1, y=1)

    # WIND
    LF_Wind = LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="blue", highlightthickness=2, height=220,
                         width=267)
    LF_Wind.place(x=613, y=101)

    # precipitation(not final)
    LF_P = LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="blue", highlightthickness=2, height=200,
                      width=267)
    LF_P.place(x=613, y=301)

    # Apperant temp (not final)
    LF_AT = LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="blue", highlightthickness=2, height=155,
                       width=267)
    LF_AT.place(x=613, y=501)

    # SUNRISE AND SUNSET
    # use pics for sunrise and sunset
    LF_Sun = LabelFrame(root1, bg = "black", relief=FLAT, highlightbackground="#2916F5", highlightthickness=2,
                        height=155, width=400)
    LF_Sun.place(x=880, y=500)

    # Humidity

    LF_Humidity = LabelFrame(root1, bg="yellow", bd="5px", relief=FLAT, highlightbackground="#2916F5",
                             highlightthickness=2, height=77, width=308)
    LF_Humidity.place(x=2, y=510)

    # UV
    LF_UV = LabelFrame(root1, bg="black", bd="5px", relief=FLAT, highlightbackground="#2916F5", highlightthickness=2,
                       height=77, width=308)
    LF_UV.place(x=2, y=580)

    # Pressure and Visibility (Not confirmed)
    LF_PV = LabelFrame(root1, bg="green", bd="5px", relief=FLAT, highlightbackground="#2916F5", highlightthickness=2,
                       height=146, width=304)
    LF_PV.place(x=310, y=510)

    LF_btn =LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="black", highlightthickness=2, height=100,
                          width=50)
    LF_btn.place(x=1200, y=10)

    btn = Button(LF_btn,
                 text="BACK",
                 command=root1.destroy)
    btn.pack()


    #img1 = PhotoImage(file='pics/sunrise.png')
    i1 = Image.open('pics/sunrise.png')
    #ph = ImageTk.PhotoImage(i1)
    r_ph = i1.resize((190, 190))
    new_image = ImageTk.PhotoImage(r_ph)
    label_image = Label(LF_Sun, image=new_image,borderwidth=0)
    label_image.pack()

    root1.mainloop()







