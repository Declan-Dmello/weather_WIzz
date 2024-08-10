from tkinter import *
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
import geocoder
import requests
from re import search
import datetime
import calendar
from data3 import *

root1 = Tk()

loc_name = "Anjuna"

# The search bar
# search_bar = Entry(root1, width=50, bg="light blue", fg="red", borderwidth="5px", relief=FLAT)
# search_bar.pack()
root1.attributes("-fullscreen", True)

# turn city names into latitudes and longitudes

# loc_name = search_bar.get()

geo = geocoder.bing(loc_name, key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
geo_results = geo.json
lat = geo_results['lat']
long = geo_results['lng']

# Getting and Modifying the API response

# WEATHER API
response1 = requests.get(
    "https://api.weatherapi.com/v1/current.json?key=b85801c481bc4e428f560932221112&q={},{}".format(lat, long))
apiWAPI = response1.json()

# Visual Crossing
response2 = requests.get(
    "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?unitGroup=metric&key=SMECUEQHNVFADAJY9MS6RUWVJ&contentType=json".format(
        lat, long))
apiVC = response2.json()

# Weather BIT
response3 = requests.get(
    "https://api.weatherbit.io/v2.0/current?&lat={}&lon={}&key=0b00917ca86543d6b7dc87fb1eaf4514".format(lat,
                                                                                                        long))
apiBIT = response3.json()

# Positon Stack
response4 = requests.get(
    "http://api.positionstack.com/v1/reverse?access_key=c71c8f5a32a2f4e942ec2facd5238ff9&query={},{}".format(lat,
                                                                                                             long))
apiPS = response4.json()

# Api Ninja
api_url = 'https://api.api-ninjas.com/v1/airquality?lat={}&lon={}'.format(lat, long)
response5 = requests.get(api_url, headers={'X-Api-Key': 'p7x7rZT5vz5vR/Bgrwc7hw==0xMYoim3COSTTrpe'})
apiAN = response5.json()

dtWAPI = apiWAPI
temp = dtWAPI["current"]["temp_c"]
feels_like = dtWAPI["current"]["feelslike_c"]
precipitation = dtWAPI["current"]["precip_mm"]
clouds = dtWAPI["current"]["cloud"]
humidity = dtWAPI["current"]["humidity"]
pressure = dtWAPI["current"]["pressure_mb"]
wind_direction = dtWAPI["current"]["wind_dir"]
wind_speed = dtWAPI["current"]["wind_kph"]
datetime1 = dtWAPI["location"]["localtime"]
date1 = datetime1[0:10]
hour = int(datetime1[11:12])

dtVC = apiVC
temp_min = dtVC["days"][0]["tempmin"]
temp_max = dtVC["days"][0]["tempmax"]

dtPS = apiPS
location = dtPS["data"][0]
locality = location["locality"]
county = location["county"]
region = location["region"]
country = location["country"]

# test Values

"""
temp = 45
datetime1 = "2022-10-02 21:35"
date1 = datetime1[0:10]
hour = 10"""

"""
temp_min = 11
temp_max = 45"""

"""  locality = "locality"
    county = "county"
    region = "region"
    country = "Country"
"""

# description = "rain"

""" feels_like = 25
precipitation = 85
clouds = 25"""

sunrise = "06:00 "
sunset = "19:30"
"""
humidity = 85
pressure = 1008"""

data = ""

visibility = 17
snow = 0

if locality is None:
    location_1 = county
else:
    location_1 = locality + "," + county

location_2 = region + "," + country

# 0-1 , 2-5 ,6-9
wind_image_list = ['pixel/forest-theme-13743738-transformed.jpeg', 'pixel/wind_s.jpg', 'pixel/wind111.jpg',
                   'pixel/wind_watermark-transformed1.jpeg']
# wind_direction = "West"

wind_description_x = 0

wind_description = ""
wind_image = ""

# wind_speed = 10

# Change text colour either fixed or acc to speed and change x cordinate
wind_speed_m = wind_speed / 1.609

wind_font_colour = ""
wind_description_colour = ""
wind_font_colour_title = ""
if wind_speed_m == 0:
    wind_description = "Calm"
    wind_description_x = 110
    wind_image = wind_image_list[0]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#008000"


elif 1 < wind_speed_m <= 4:
    wind_description = "Light Air"
    wind_description_x = 90
    wind_image = wind_image_list[0]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#008000"

elif 4 < wind_speed_m <= 8:
    wind_description = "Light Breeze"
    wind_description_x = 65
    wind_image = wind_image_list[1]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#006400"

elif 8 < wind_speed_m <= 13:
    wind_description = "Gentle Breeze"
    wind_description_x = 50
    wind_image = wind_image_list[1]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#006400"

elif 13 < wind_speed_m <= 19:
    wind_description = "Moderate Breeze"
    wind_description_x = 40
    wind_image = wind_image_list[1]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#006400"

elif 19 < wind_speed_m <= 25:
    wind_description = "Fresh Breeze"
    wind_description_x = 55
    wind_image = wind_image_list[1]
    wind_font_colour_title = "#2B65EC"
    wind_font_colour = "white"
    wind_description_colour = "#006400"

elif 25 < wind_speed_m <= 32:
    wind_description = "Strong Breeze"
    wind_description_x = 52
    wind_image = wind_image_list[2]
    wind_font_colour_title = "#1589FF"
    wind_font_colour = "#2E8B57"
    wind_description_colour = "White"

elif 32 < wind_speed_m <= 39:
    wind_description = "Near Gale"
    wind_description_x = 75
    wind_image = wind_image_list[2]
    wind_font_colour_title = "#1589FF"
    wind_font_colour = "#2E8B57"
    wind_description_colour = "White"

elif 39 < wind_speed_m <= 47:
    wind_description = "Gale"
    wind_description_x = 118
    wind_image = wind_image_list[2]
    wind_font_colour_title = "#1589FF"
    wind_font_colour = "#2E8B57"
    wind_description_colour = "White"

elif 47 < wind_speed_m <= 55:
    wind_description = "Strong Gale"
    wind_description_x = 70
    wind_image = wind_image_list[2]
    wind_font_colour_title = "#1589FF"
    wind_font_colour = "#2E8B57"
    wind_description_colour = "White"

elif 55 < wind_speed_m <= 64:
    wind_description = "Whole Gale"
    wind_description_x = 70
    wind_image = wind_image_list[3]
    wind_font_colour_title = "#8EEBEC"
    wind_font_colour = "#8EEBEC"
    wind_description_colour = "#FF5F1F"

elif 64 < wind_speed_m <= 75:
    wind_description = "Storm Force"
    wind_description_x = 70
    wind_image = wind_image_list[3]
    wind_font_colour_title = "#8EEBEC"
    wind_font_colour = "#8EEBEC"
    wind_description_colour = "#F62817"

elif 75 < wind_speed_m:
    wind_description = "Hurricane Force"
    wind_description_x = 40
    wind_image = wind_image_list[3]
    wind_font_colour_title = "#8EEBEC"
    wind_font_colour = "#8EEBEC"
    wind_description_colour = "#F62817"

dtBIT = apiBIT
description = dtBIT["data"][0]["weather"]["description"]

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

# WIDGETS
# Time on top and date below it

# TITLE BAR

LF_Title = LabelFrame(root1, bd="5px", relief=FLAT, highlightbackground="black", highlightthickness=2, height=101,
                      width=1278)
LF_Title.place(x=1, y=2)

LF_head = LabelFrame(root1, bg="light blue", bd="1px", relief=FLAT, highlightbackground="black", height=100,
                     width=1030)
LF_head.place(x=125, y=2)

head_label = Label(LF_head, text="CURRENT   WEATHER", bg="light blue", font=("bahnschrift", 65)).place(x=70, y=-5)

"""def refresher():
    global data
    response = requests.get("http://worldtimeapi.org/api/timezone/America/Argentina/Salta")
    data = response.json()
    timeApi0 = data['datetime'][12:19]
    # timeApi0 = "11:23"
    timeApi = timeApi0.replace(":", " : ")
    dateApi = data['datetime'][0:10]
    #dateApi = "22-12-2022"
    time_label.configure(text=timeApi)
    LF_time.after(5000, refresher)
    return dateApi
"""

LF_time = LabelFrame(root1, bg="black", bd="2px", relief=FLAT, highlightbackground="black", height=50,
                     width=120)
LF_time.place(x=0, y=2)

time_label = Label(LF_time, foreground="red", background="black", font=("bahnschrift", 25))
time_label.pack()

date1 = 10  # refresher()

LF_date = LabelFrame(root1, bg="black", bd="2px", relief=FLAT, highlightbackground="black", height=50,
                     width=120)
LF_date.place(x=0, y=53)

date_label = Label(LF_date, text=date1, foreground="black", background="light blue", font=("bahnschrift", 25))
date_label.pack()

# Back button
LF_btn = LabelFrame(root1, bg="black", bd="1px", relief=FLAT, highlightbackground="black", height=100,
                    width=100)
LF_btn.place(x=1145, y=2)

back_icon = Image.open("pixel/backbutton.webp")

# Resize the image in the given (width, height)
r_back_icon = back_icon.resize((127, 95))

back_icon_im = ImageTk.PhotoImage(r_back_icon)

btn = Button(LF_btn, text="BACK", image=back_icon_im,
             command=root1.destroy, height=95, width=127, bg="white", relief=FLAT,
             activebackground="white")  # RIDGE , GROOVE , SUNKEN
btn.pack()

# AQI WIDGET
dtAN = apiAN

AQI = dtAN["overall_aqi"]

# AQI = 50

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

LF_AQI = LabelFrame(root1, bg=bg_colour, relief=FLAT, highlightbackground="black", highlightthickness=2,
                    height=410, width=400)  # border thickness
LF_AQI.place(x=880, y=100)  # 880

# LABELS
Label(LF_AQI, text="AIR   QUALITY   INDEX", bg=bg_colour, font=("bahnschrift", 20), fg=title_font).place(x=55, y=50)

Label(LF_AQI, text=AQI, bg=bg_colour, font=("Sans-serif", 60), fg=AQI_fg_colour).place(x=AQI_x, y=120)

Label(LF_AQI, text=AQI_description, bg=bg_colour, font=("bahnschrift", 30), fg=AQI_description_fg).place(
    x=AQI_description_x, y=220)

Label(LF_AQI, text=AQI_Health_Advice, bg=bg_colour, font=8, fg=AQI_HA_fg).place(x=AQI_HA_x, y=280)

# image widget customization
# The font
txt1 = 'arial.ttf'
txt = 'vera.ttf'

# add text to image
font = ImageFont.truetype(txt1, 60)
font1 = ImageFont.truetype(txt, 25)
font2 = ImageFont.truetype(txt, 18)
font3 = ImageFont.truetype(txt1, 25)
font4 = ImageFont.truetype(txt1, 35)

# IMAGE WIDGETS

# CURRENT WEATHER WIDGET
# Image1
# Creating a LabelFrame

LF_CW = LabelFrame(root1, bg="black", relief=FLAT)
LF_CW.place(x=0, y=100)

# Opening an image from the List

Widget_CW = Image.open(Labelframe_image)
resized_CW = Widget_CW.resize((606, 404), Image.ANTIALIAS)
# draw image object
I1 = ImageDraw.Draw(resized_CW)

# Modifying and displaying the ext data
I1.text((25, 260), str(temp), font=font, fill="#FFFFFF")
I1.text((150, 270), "°C", font=font2, fill="#FFFFFF")
I1.text((25, 330), str(DT), font=font2, fill="#FFFFFF")
I1.text((150, 288), str(description), font=font1, fill="#FFFFFF")
I1.text((150, 330), str(temp_min_max), font=font2, fill="#FFFFFF")
I1.text((25, 10), str(location_1), font=font2, fill="#FF6700")
I1.text((25, 30), str(location_2), font=font2, fill="#FF6700")

new_resized_CW = ImageTk.PhotoImage(resized_CW)
label_image_widget_CW = Label(LF_CW, image=new_resized_CW, borderwidth=0)
label_image_widget_CW.grid(row=5, column=5)

# FEELS LIKE
# Image 2
LF_Feels_like = LabelFrame(root1, bg="black", relief=FLAT,
                           height=220,
                           width=267)
LF_Feels_like.place(x=608, y=100)

widget_Feels_like = Image.open('pixel/u2ssrbzynal41.png')

resized_Feels_like = widget_Feels_like.resize((270, 198), Image.ANTIALIAS)

I2 = ImageDraw.Draw(resized_Feels_like)

feels_like_font = ImageFont.truetype(txt1, 40)
feels_like_font1 = ImageFont.truetype(txt1, 35)

I2.text((50, 20), "Feels Like", font=feels_like_font, fill="#F9DB24")
I2.text((85, 70), str(feels_like), font=feels_like_font1, fill="#F9DB24")

new_resized_Feels_like = ImageTk.PhotoImage(resized_Feels_like)
label_image_widget_Feels_like = Label(LF_Feels_like, image=new_resized_Feels_like, borderwidth=0)
label_image_widget_Feels_like.pack()

# precipitation , clouds
# Image 3
LF_P = LabelFrame(root1, bg="black", relief=FLAT,
                  height=209, width=267)
LF_P.place(x=608, y=300)

widget_cloud = Image.open('pixel/pixel-art-complex-cloud-sky_150088-733.webp')

resized_cloud = widget_cloud.resize((270, 205), Image.ANTIALIAS)

I3 = ImageDraw.Draw(resized_cloud)

cloud_font = ImageFont.truetype(txt1, 40)
cloud_font1 = ImageFont.truetype(txt1, 35)

I3.text((65, 5), "Clouds", font=cloud_font, fill="#00BFFF")
I3.text((95, 50), str(clouds), font=cloud_font1, fill="#00BFFF")
I3.text((30, 110), "Precipitation", font=cloud_font, fill="#1E90FF")
I3.text((95, 155), str(precipitation), font=cloud_font1, fill="#1E90FF")

new_resized_cloud = ImageTk.PhotoImage(resized_cloud)
label_image_widget_cloud = Label(LF_P, image=new_resized_cloud, borderwidth=0)
label_image_widget_cloud.pack()

# WIND
# Image 4

# if wind speed above certain km per hour then change bg image , calm pic , windy pic , fast wind pic already downloaded
LF_Wind = LabelFrame(root1, bg="black", relief=FLAT,
                     height=108,
                     width=308)
LF_Wind.place(x=303, y=506)

widget_wind_image = Image.open(wind_image)

resized_wind = widget_wind_image.resize((303, 210), Image.ANTIALIAS)

I4 = ImageDraw.Draw(resized_wind)

wind_font = ImageFont.truetype(txt1, 45)
wind_font1 = ImageFont.truetype(txt1, 30)

I4.text((95, 5), "Wind ", font=wind_font, fill=wind_font_colour_title)
I4.text((40, 50), "Speed", font=wind_font1, fill=wind_font_colour)
I4.text((190, 50), str(wind_speed) + " km/h", font=wind_font1, fill=wind_font_colour)
I4.text((40, 90), "Direction", font=wind_font1, fill=wind_font_colour)
I4.text((200, 90), str(wind_direction), font=wind_font1, fill=wind_font_colour)
I4.text((wind_description_x, 160), str(wind_description), font=wind_font1, fill=wind_description_colour)

new_resized_wind = ImageTk.PhotoImage(resized_wind)
label_image_widget_wind = Label(LF_Wind, image=new_resized_wind, borderwidth=0)
label_image_widget_wind.pack()

# SUNRISE
# Image 5
LF_Sunrise = LabelFrame(root1, bg="black", relief=FLAT,
                        height=220, width=400)
LF_Sunrise.place(x=880, y=508)

widget_sunrise = Image.open('pics/sunrise.png')

resized_sunrise = widget_sunrise.resize((198, 208), Image.ANTIALIAS)

I5 = ImageDraw.Draw(resized_sunrise)

sunrise_font = ImageFont.truetype(txt1, 45)
sunrise_font1 = ImageFont.truetype(txt1, 35)

I5.text((26, 20), "Sunrise", font=sunrise_font, fill="#F5E216")
I5.text((25, 150), sunrise + " Am", font=sunrise_font1, fill="#FFEF00")

new_resized_sunrise = ImageTk.PhotoImage(resized_sunrise)
label_image_widget_sunrise = Label(LF_Sunrise, image=new_resized_sunrise, borderwidth=0)
label_image_widget_sunrise.pack()

# SUNSET
# Image6
LF_Sunset = LabelFrame(root1, bg="black", relief=FLAT,
                       height=220, width=400)
LF_Sunset.place(x=1079, y=508)

widget_sunset = Image.open('pics/sunset.png')

resized_sunset = widget_sunset.resize((197, 208), Image.ANTIALIAS)

I6 = ImageDraw.Draw(resized_sunset)

sunset_font = ImageFont.truetype(txt1, 45)
sunset_font1 = ImageFont.truetype(txt1, 35)

I6.text((26, 20), "Sunset", font=sunset_font, fill="red")
I6.text((25, 150), sunset + " Pm", font=sunset_font1, fill="#DC381F")

new_resized_sunset = ImageTk.PhotoImage(resized_sunset)
label_image_widget_sunset = Label(LF_Sunset, image=new_resized_sunset, borderwidth=0)
label_image_widget_sunset.pack()

# Visibility
# Image 7
LF_Visibility = LabelFrame(root1, bg="black", relief=FLAT,
                           height=105,
                           width=230)
LF_Visibility.place(x=608, y=506)

widget_Visibility = Image.open('pixel/low-visibility-driving.jpg')

resized_Visibility = widget_Visibility.resize((270, 104), Image.ANTIALIAS)

I7 = ImageDraw.Draw(resized_Visibility)

visibility_font = ImageFont.truetype(txt1, 35)
visibility_font1 = ImageFont.truetype(txt1, 35)

I7.text((70, 5), "Visibility", font=visibility_font, fill="#FF6347")
I7.text((75, 60), str(visibility) + " Km", font=visibility_font1, fill="#FF6347")

new_resized_Visibility = ImageTk.PhotoImage(resized_Visibility)
label_image_widget_visibility = Label(LF_Visibility, image=new_resized_Visibility, borderwidth=0)
label_image_widget_visibility.pack()

# Snow
# Image 8
LF_Snow = LabelFrame(root1, bg="black", relief=FLAT,
                     height=105, width=267)
LF_Snow.place(x=608, y=611)

widget_snow = Image.open('pixel/snoww2.png')

resized_snow = widget_snow.resize((270, 105), Image.ANTIALIAS)

I8 = ImageDraw.Draw(resized_snow)

snow_font = ImageFont.truetype(txt1, 35)
snow_font1 = ImageFont.truetype(txt1, 35)

I8.text((90, 5), "Snow", font=snow_font, fill="white")
I8.text((105, 60), str(snow) + " in", font=snow_font1, fill="white")

new_resized_snow = ImageTk.PhotoImage(resized_snow)
label_image_widget_snow = Label(LF_Snow, image=new_resized_snow, borderwidth=0)
label_image_widget_snow.pack()

# Humidity
# Image 9
LF_Humidity = LabelFrame(root1, bg="black", relief=FLAT,
                         height=105, width=304)
LF_Humidity.place(x=0, y=506)

widget_Humidity = Image.open('pixel/What-Happens-When-You-Paint-in-High-Humidity.webp')

resized_Humidity = widget_Humidity.resize((301, 107), Image.ANTIALIAS)

I9 = ImageDraw.Draw(resized_Humidity)

humidity_font = ImageFont.truetype(txt1, 35)
humidity_font1 = ImageFont.truetype(txt1, 35)

I9.text((80, 5), "Humidity", font=humidity_font, fill="#FFA62F")
I9.text((120, 60), str(humidity) + "%", font=humidity_font1, fill="#FFA62F")

new_resized_Humidity = ImageTk.PhotoImage(resized_Humidity)
label_image_widget_Humidity = Label(LF_Humidity, image=new_resized_Humidity, borderwidth=0)
label_image_widget_Humidity.pack()

# Pressure
# Image 10
LF_Pressure = LabelFrame(root1, bg="black", relief=FLAT,
                         height=105, width=304)
LF_Pressure.place(x=0, y=615)

widget_Pressure = Image.open('pixel/pressure.png')

resized_Pressure = widget_Pressure.resize((301, 107), Image.ANTIALIAS)

I10 = ImageDraw.Draw(resized_Pressure)

pressure_font = ImageFont.truetype(txt1, 30)
pressure_font1 = ImageFont.truetype(txt1, 30)

I10.text((80, 5), "Pressure", font=pressure_font1, fill="red")
I10.text((85, 60), str(pressure) + " mb", font=pressure_font, fill="red")

new_resized_Pressure = ImageTk.PhotoImage(resized_Pressure)
label_image_widget_Pressure = Label(LF_Pressure, image=new_resized_Pressure, borderwidth=0)
label_image_widget_Pressure.pack()

mainloop()



