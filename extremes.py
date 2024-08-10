import pandas as pd
from tkinter import *
import requests
import geocoder
import csv
import urllib.request
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.ticker as plticker
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
import tkinter.font as tkFont

def extreme():

    wi =Toplevel()
    wi.attributes('-fullscreen', True)




    url = "https://www.weather-forecast.com/"
    
    with urllib.request.urlopen(url) as i:
        html = i.read()
    
    data = pd.read_html(html)[6]
    
    data.to_csv("programming.csv")
    
    
    
    file = open('programming.csv')
    csvreader = csv.reader(file)
    
    header = list(next(csvreader))
    
    rows = []
    
    for row in csvreader:
        rows.append(row)
    
    
    hottest_list=""
    coldest_list=""
    wettest_list=""
    windiest_list=""
    
    for i in rows:
        hottest_list =list(rows[1])
        coldest_list =list(rows[3])
        wettest_list =list(rows[5])
        windiest_list =list(rows[7])
    
    header.pop(0)
    hottest_list.pop(0)
    coldest_list.pop(0)
    wettest_list.pop(0)
    windiest_list.pop(0)
    
    
    for i in hottest_list:
        hottest_list[hottest_list.index(i)] = i[:-4] + i[-2:]
    for i in coldest_list:
        coldest_list[coldest_list.index(i)] = i[:-4] + i[-2:]

    # hottest

    ht_name = []
    ht_data = []
    ht_temp = []
    for i in hottest_list:
        ht_name.append(i.split("high"))

    for i in ht_name:
        if len(i) > 20:
            ht_temp.append(i.split(" "))
            ht_name.insert(windiest_list.index(i), (ht_temp[0][0]))
        else:
            ht_data.append(i[1])
            ht_name[ht_name.index(i)] = i[0]

    # coldest

    cd_name = []
    cd_data = []
    cd_temp = []
    for i in coldest_list:
        cd_name.append(i.split("low"))

    for i in cd_name:
        if len(i) > 20:
            cd_temp.append(i.split(" "))
            cd_name.insert(windiest_list.index(i), (cd_temp[0][0]))
        else:
            cd_data.append(i[1])
            cd_name[cd_name.index(i)] = i[0]

    # rain/wettest
    pos = 0
    wt_name = []
    wt_data = []
    wt_temp = []
    for i in wettest_list:
        if len(i[:-7]) > 20:
            wt_temp.append(i.split(" "))
            wt_name.insert(windiest_list.index(i), (wt_temp[0][0]))
        elif i == '':
            wt_name.append("Data not Available")
            pos = wettest_list.index(i)
        else:
            wt_name.append(i.split(" "))

    for i in wt_name:
        if i == "Data not Available":
            wt_data.insert(pos, i[-10:])
            wt_name[wt_name.index(i)] = i[:-10]
        elif i[2] == '':
            wt_data.append(i[3] + " " + i[4])  # adds the number and measurement
            wt_name[wt_name.index(i)] = i[0] + " " + i[1]
        else:
            wt_data.append(i[2] + " " + i[3])
            wt_name[wt_name.index(i)] = i[0] + " " + i[1]

    # windiest
    wd_name = []
    wd_data = []

    wd_temp = []

    for i in windiest_list:
        if len(i[:-7]) > 20:
            wd_temp.append(i.split(" "))
            wd_name.insert(windiest_list.index(i), (wd_temp[0][0]))
            wd_data.append(i[-7:])
        else:
            wd_data.append(i[-7:])
            wd_name.append(i[:-7])

    #wi.attributes("-fullscreen", True)
    
    response_FLI= requests.get("https://api.tomorrow.io/v4/timelines?location=20.5937,78.9629&fields=floodIndex&units=metric&timesteps=1h&startTime=now&endTime=nowPlus17h&apikey=2A6CqWS6pDWNjPVC8P0AfMh7Kl7AgVWq")
    response_FII= requests.get("https://api.tomorrow.io/v4/timelines?location=20.5937,78.9629&fields=fireIndex&units=metric&timesteps=1h&startTime=now&endTime=nowPlus17h&apikey=2A6CqWS6pDWNjPVC8P0AfMh7Kl7AgVWq")
    
    apiFL = response_FLI.json()
    apiFi = response_FII.json()
    
    flood_data = apiFL["data"]["timelines"][0]["intervals"]
    fire_data = apiFi["data"]["timelines"][0]["intervals"]
    
    flood_index= [ ]
    f_time= [ ]
    
    for i in flood_data:
        f_time.append(i["startTime"][11:-4])
        flood_index.append(i["values"]["floodIndex"])
    
    fire_index= [ ]
    
    for i in fire_data:
        fire_index.append(i["values"]["fireIndex"])
    
    dates= []
    for i in header:
        dates.append(i)

    table_colour = "#87CEFA"
    font5 = tkFont.Font(family="Comic Sans MS", size=18, weight="bold")
    font6 = tkFont.Font(family="Comic Sans MS", size=60, weight="bold")
    font7 = tkFont.Font(family="Comic Sans MS", size=26, weight="bold")

    table_filler_F = Frame(wi, background="#306EFF", height=350, width=1280).place(x=0, y=100)

    title_bar = Frame(wi, background="#306EFF", height=110, width=1280).place(x=0, y=0)

    table_border_F = Frame(wi, background="black", height=277, width=1102).place(x=88, y=133.5)

    #btn_table_left = Frame(wi, background="#CCCCFF", height=250, width=60).place(x=5, y=148)

    #btn_table_right = Frame(wi, background="#CCCCFF", height=250, width=60).place(x=1210, y=148)

    title_label = Label(wi,background="#306EFF",text="WEATHER   EXTREMES",font=font6).place(x=80,y=5)


    # 3 buttons both sides
    widget_x1 = [90, 273, 456, 639, 822, 1005]
    widget_x2 = [100, 285, 490, 660, 830, 1010]
    widget_x3 = [110, 330, 515, 695, 880, 1060]

    txt1 = 'arial.ttf'
    txt = 'vera.ttf'

    for i in range(0, 6):
        x1 = widget_x1[i]
        x2 = widget_x2[i]
        x3 = widget_x3[i]
        # title - date - type - data
        Frame(wi, background=table_colour, height=67, width=183).place(x=x1, y=135)
        Frame(wi, background=table_colour, height=52, width=183, highlightbackground="black", highlightthickness=1).place(x=x1,
                                                                                                                     y=203)
        Label(wi, text=dates[i], background=table_colour,font=font5).place(x=x3, y=213)


    def table_extreme_hottest():
        for i in range(0, 6):
            x1 = widget_x1[i]
            x2 = widget_x2[i]
            # title - date - type - data
            Frame(wi, background=table_colour, height=52, width=183).place(x=x1, y=256)
            Frame(wi, background=table_colour, height=101, width=183, highlightbackground="black", highlightthickness=1).place(
                x=x1, y=309)
            Label(wi, text=ht_name[i], font=  font5, background=table_colour, foreground="#B22222").place(x=x2, y=320)
            Label(wi, text=ht_data[i], font=  font5, background=table_colour, foreground="#B22222").place(x=x2, y=365)
            Label(wi, text="HOTTEST", font=   font5,background=table_colour, foreground="#B22222").place(x=550, y=265)



    def table_extreme_coldest():
        for i in range(0, 6):
            x1 = widget_x1[i]
            x2 = widget_x2[i]
            # title - date - type - data
            Frame(wi, background=table_colour, height=52, width=183).place(x=x1, y=256)
            Frame(wi, background=table_colour, height=101, width=183, highlightbackground="black", highlightthickness=1).place(
                x=x1, y=309)
            Label(wi, text=cd_name[i], font=font5, background=table_colour).place(x=x2, y=320)
            Label(wi, text=cd_data[i], font=font5, background=table_colour).place(x=x2, y=365)
            Label(wi, text="COLDEST", font= font5, background=table_colour).place(x=550, y=265)


    def table_extreme_windiest():
        for i in range(0, 6):
            x1 = widget_x1[i]
            x2 = widget_x2[i]
            # title - date - type - data
            Frame(wi, background=table_colour, height=52, width=183).place(x=x1, y=256)
            Frame(wi, background=table_colour, height=101, width=183, highlightbackground="black",
                  highlightthickness=1).place(x=x1, y=309)
            Label(wi, text=wd_name[i],foreground="#1E90FF" ,font=font5, background=table_colour).place(x=x2, y=320)
            Label(wi, text=wd_data[i],foreground="#1E90FF", font=font5, background=table_colour).place(x=x2, y=365)
            Label(wi, text="WINDIEST",foreground="#1E90FF", font=font5, background=table_colour).place(x=550, y=265)


    def table_extreme_wettest():
        for i in range(0, 6):
            x1 = widget_x1[i]
            x2 = widget_x2[i]
            # title - date - type - data
            Frame(wi, background=table_colour, height=52, width=183).place(x=x1, y=256)
            Frame(wi, background=table_colour, height=101, width=183, highlightbackground="black", highlightthickness=1).place(
                x=x1, y=309)
            Label(wi, text=wt_name[i],foreground="#0909FF" ,background=table_colour, font=font5).place(x=x2, y=320)
            Label(wi, text=wt_data[i],foreground="#0909FF", background=table_colour, font=font5).place(x=x2, y=365)
            Label(wi, text="WETTEST",foreground="#0909FF", font=font5, background=table_colour).place(x=550, y=265)


    table_extreme_hottest()

    Label(wi, text="India Temperature Extreme", background=table_colour, font=font7).place(x=280, y=140)

    fire_graph = dict(zip(f_time, fire_index))
    flood_graph = dict(zip(f_time, flood_index))


    def plot1():
        fig = Figure((18, 6), dpi=85)

        x = fire_graph.keys()
        y = fire_graph.values()

        plot1 = fig.add_subplot(211)
        plot1.set_title("Graph Displaying Fire Danger")
        plot1.set_xlabel("Time of Day")
        plot1.set_ylabel("Fire Index")
        plot1.set_ylim(0, 50)
        loc = plticker.MultipleLocator(base=1.0)

        plot1.xaxis.set_major_locator(loc)

        plot1.plot(x, y, color="red", marker='o')

        for x, y in zip(x, y):
            label = "{}".format(y)
            plot1.annotate(label, xy=(x, y), textcoords='offset points', xytext=(0, 10), ha='center')

        canvas1 = FigureCanvasTkAgg(fig, master=wi)
        canvas1.draw()

        canvas1.get_tk_widget().place(x=-125, y=420)


    def plot2():
        fig = Figure((18, 6), dpi=85)

        x = flood_graph.keys()
        y = flood_graph.values()

        plot2 = fig.add_subplot(211)
        plot2.set_title("Graph Displaying Flood Danger")
        plot2.set_xlabel("Time of Day")
        plot2.set_ylabel("Fire Index")
        plot2.set_ylim(0, 50)
        loc = plticker.MultipleLocator(base=1.0)

        plot2.xaxis.set_major_locator(loc)

        plot2.plot(x, y, color="blue", marker='o')

        for x, y in zip(x, y):
            label = "{}".format(y)
            plot2.annotate(label, xy=(x, y), textcoords='offset points', xytext=(0, 10), ha='center')

        canvas2 = FigureCanvasTkAgg(fig, master=wi)
        canvas2.draw()

        canvas2.get_tk_widget().place(x=-125, y=420)
    plot1()


    #Fire
    img_fire = Image.open("pixel/png-transparent-fire-illustration-fire-cartoon-flame-fire-cartoon-silhouette-orange-computer-wallpaper-desktop-wallpaper-thumbnail-removebg-preview.png")
    resize_img_fire = img_fire.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_fire = ImageTk.PhotoImage(resize_img_fire)


    #Flood
    img_flood = Image.open("pixel/flood-graphic.png")
    resize_img_flood = img_flood.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_flood = ImageTk.PhotoImage(resize_img_flood)

    # Heat
    img_heat = Image.open("pixel/thermometer-sun-heat-temperature-icon-vector-22773423.jpg")
    resize_img_heat = img_heat.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_heat = ImageTk.PhotoImage(resize_img_heat)

    #Cold

    img_cold = Image.open("pixel/157-1575741_snow-snowflake-cartoon-removebg-preview.png")
    resize_img_cold = img_cold.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_cold = ImageTk.PhotoImage(resize_img_cold)

    #Wind
    img_wind = Image.open("pixel/168-1686015_catoon-wind-wind-swirl-clipart-removebg-preview.png")
    resize_img_wind = img_wind.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_wind = ImageTk.PhotoImage(resize_img_wind)

    #rain
    img_wet = Image.open("pixel/png-cartoon-cloud-rain-icon-31630923088ab1ube2pw4.png")
    resize_img_wet = img_wet.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_wet = ImageTk.PhotoImage(resize_img_wet)

    #EXIT
    img_bck = Image.open("pixel/bck-removebg-preview(1).png")
    resize_img_bck = img_bck.resize((105, 96), Image.ANTIALIAS)
    new_resized_img_bck = ImageTk.PhotoImage(resize_img_bck)

    btn = Button(wi, image=new_resized_img_fire, command=plot1, relief=FLAT,highlightthickness=0)
    btn.place(x=1220, y=280)

    btn1 = Button(wi, image=new_resized_img_flood, command=plot2, relief=FLAT,highlightthickness=0)
    btn1.place(x=1220, y=355)

    btn2 = Button(wi,image=new_resized_img_bck, command=wi.destroy, relief=FLAT,highlightthickness=0, background="#306EFF" )
    btn2.place(x=1145, y=4)

    btn3 = Button(wi, image=new_resized_img_heat, command=table_extreme_hottest, relief=FLAT,highlightthickness=0)
    btn3.place(x=16, y=160)

    btn4 = Button(wi, image=new_resized_img_cold, command=table_extreme_coldest, relief=FLAT,highlightthickness=0)
    btn4.place(x=16, y=225)

    btn5 = Button(wi, image=new_resized_img_wind, command=table_extreme_windiest, relief=FLAT,highlightthickness=0)
    btn5.place(x=16, y=290)

    btn6 = Button(wi,image=new_resized_img_wet, command=table_extreme_wettest, relief=FLAT,highlightthickness=0)
    btn6.place(x=16, y=355)


    mainloop()

