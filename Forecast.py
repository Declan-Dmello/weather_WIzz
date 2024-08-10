from tkinter import *
from PIL import Image, ImageTk

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

import matplotlib.ticker as plticker
import datetime
import calendar
import requests
import geocoder
import tkinter.font as tkFont

# change colour of graph if suitable
# bind keys ti
def forecast(value):
    window = Toplevel()

    global val1
    val1 = value

    loc_name1 = val1

    geo = geocoder.bing(loc_name1, key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
    geo_results = geo.json
    lat = geo_results['lat']
    long = geo_results['lng']



    window.attributes("-fullscreen", True)

    # npotes for me , put the x cordinates of the conditions with 3 elements

    # setting the title
    window.title('Plotting in Tkinter')

    # dimensions of the main window

    #put a line above buttons , near the buttons do hourly: (Text refreshing on clicks )

    # max , min , icon,date
    # hours
    # Visual Crossing



    response2 = requests.get(
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{},{}?unitGroup=metric&key=RL2SXLMPHJ6JWUPAG7DPQ6LBJ&contentType=json".format(
            lat, long))
    apiVC = response2.json()

    all_days = apiVC["days"]
    all_hours = apiVC["days"][0]["hours"]

    day_0 = all_days[1]
    day_0_date = day_0["datetime"]
    day_0_icon = ""
    day_0_condition = day_0["conditions"]

    day_0_max = day_0["tempmax"]
    day_0_min = day_0["tempmin"]
    year, month, day = map(int, day_0_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_0 = calendar.day_name[my_date.weekday()]
    f_date_0 = ("{}-{}-{}".format(day, month, year))

    day_1 = all_days[2]
    day_1_date = day_1["datetime"]
    day_1_icon = ""
    day_1_condition = day_1["conditions"]
    day_1_max = day_1["tempmax"]
    day_1_min = day_1["tempmin"]
    year, month, day = map(int, day_1_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_1 = calendar.day_name[my_date.weekday()]
    f_date_1 = ("{}-{}-{}".format(day, month, year))

    day_2 = all_days[3]
    day_2_date = day_2["datetime"]
    day_2_icon = ""
    day_2_condition = day_2["conditions"]
    day_2_max = day_2["tempmax"]
    day_2_min = day_2["tempmin"]
    year, month, day = map(int, day_2_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_2 = calendar.day_name[my_date.weekday()]
    f_date_2 = ("{}-{}-{}".format(day, month, year))

    day_3 = all_days[4]
    day_3_date = day_3["datetime"]
    day_3_icon = ""
    day_3_condition = day_3["conditions"]
    day_3_max = day_3["tempmax"]
    day_3_min = day_3["tempmin"]
    year, month, day = map(int, day_3_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_3 = calendar.day_name[my_date.weekday()]
    f_date_3 = ("{}-{}-{}".format(day, month, year))

    day_4 = all_days[5]
    day_4_date = day_4["datetime"]
    day_4_icon = ""
    day_4_condition = day_4["conditions"]
    day_4_max = day_4["tempmax"]
    day_4_min = day_4["tempmin"]
    year, month, day = map(int, day_4_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_4 = calendar.day_name[my_date.weekday()]
    f_date_4 = ("{}-{}-{}".format(day, month, year))

    day_5 = all_days[6]
    day_5_date = day_5["datetime"]
    day_5_icon = ""
    day_5_condition = day_5["conditions"]
    day_5_max = day_5["tempmax"]
    day_5_min = day_5["tempmin"]
    year, month, day = map(int, day_5_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_5 = calendar.day_name[my_date.weekday()]
    f_date_5 = ("{}-{}-{}".format(day, month, year))

    day_6 = all_days[7]
    day_6_date = day_6["datetime"]
    day_6_icon = ""
    day_6_condition = day_6["conditions"]
    day_6_max = day_6["tempmax"]
    day_6_min = day_6["tempmin"]
    year, month, day = map(int, day_6_date.split("-"))  # breaks into
    my_date = datetime.date(year, month, day)
    weekday_6 = calendar.day_name[my_date.weekday()]
    f_date_6 = ("{}-{}-{}".format(day, month, year))

    condition_x_0 = 0
    condition_x_1 = 0
    condition_x_2 = 0
    condition_x_3 = 0
    condition_x_4 = 0
    condition_x_5 = 0
    condition_x_6 = 0

    l0 = list(day_0_condition.split(","))
    day_0_c_f = l0[0]

    l1 = list(day_1_condition.split(","))
    day_1_c_f = l1[0]

    l2 = list(day_2_condition.split(","))
    day_2_c_f = l2[0]

    l3 = list(day_3_condition.split(","))
    day_3_c_f = l3[0]

    l4 = list(day_4_condition.split(","))
    day_4_c_f = l4[0]

    l5 = list(day_5_condition.split(","))
    day_5_c_f = l5[0]

    l6 = list(day_6_condition.split(","))
    day_6_c_f = l6[0]

    # clear, partlycloud , cloud , rain , snow,thunderstorm
    forecast_img_list = ["pixel/sunny.png", "pixel/partly_cloudy_day_sun_clouds_weather_icon_177560(1).png",
                         "pixel/cloudy.png", "pixel/rain.png", "pixel/snow.png",
                         "pixel/thunderstorm.png","pixel/cloudy.png"
                         ]

    forecast_weather = ["Clear", "Partially cloudy", "Cloudy", "Rain", "Snow", "Thunderstorm", "Overcast"]

    weekday_list = [weekday_0, weekday_1, weekday_2, weekday_3, weekday_4, weekday_5, weekday_6]

    for i in forecast_weather:
        if day_0_c_f == i:
            index_0 = forecast_weather.index(i)
            day_0_icon = forecast_img_list[index_0]
        if day_1_c_f == i:
            index_1 = forecast_weather.index(i)
            day_1_icon = forecast_img_list[index_1]
        if day_2_c_f == i:
            index_2 = forecast_weather.index(i)
            day_2_icon = forecast_img_list[index_2]
        if day_3_c_f == i:
            index_3 = forecast_weather.index(i)
            day_3_icon = forecast_img_list[index_3]
        if day_4_c_f == i:
            index_4 = forecast_weather.index(i)
            day_4_icon = forecast_img_list[index_4]
        if day_5_c_f == i:
            index_5 = forecast_weather.index(i)
            day_5_icon = forecast_img_list[index_5]
        if day_6_c_f == i:
            index_6 = forecast_weather.index(i)
            day_6_icon = forecast_img_list[index_6]

    if len(l0) > 1:
        day_0_c_f = day_0_c_f + l0[1]
        condition_x_0 = 0
    else:
        condition_x_0 = 15

    if len(l1) > 1:
        day_1_c_f = day_1_c_f + l1[1]
        condition_x_1 = 0
    else:
        condition_x_1 = 15

    if len(l2) > 1:
        day_2_c_f = day_2_c_f + l2[1]
        condition_x_2 = 0
    else:
        condition_x_2 = 15

    if len(l3) > 1:
        day_3_c_f = day_3_c_f + l3[1]
        condition_x_3 = 0
    else:
        day_3_c_f = day_3_condition
        condition_x_3 = 15

    if len(l4) > 1:
        day_4_c_f = day_4_c_f + l4[1]
        condition_x_4 = 0
    else:
        day_4_c_f = day_4_condition
        condition_x_4 = 15

    if len(l5) > 1:
        day_5_c_f = day_5_c_f + l5[1]
        condition_x_5 = 0
    else:
        day_5_c_f = day_5_condition
        condition_x_5 = 15

    if len(l6) > 1:
        day_6_c_f = day_6_c_f + l6[1]
        condition_x_6 = 0
    else:
        day_6_c_f = day_6_condition
        condition_x_6 = 15


    font_fore = tkFont.Font(family="Comic Sans MS", size=50, weight="bold")


    Frame(window,height =  90, width =1280,background= "white").place(x=0, y =0)
    Label(window, text="  WEATHER   FORECAST",background="white",font=font_fore).place(x=200,y=-3)




    main_forecast = LabelFrame(window, height=245, width=1280, background="black", bd="3px", relief=FLAT)
    main_forecast.place(x=0, y=95)

    # Widget1


    F_forecast_widget_1 = Frame(window, height=220, width=155, background="white", relief=FLAT)
    F_forecast_widget_1.place(x=20, y=107)

    canvas1 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas1.place(x=32, y=160)

    img_1 = PhotoImage(file=day_0_icon)
    canvas1.create_image(65, 50, image=img_1)

    label_forecast_widget1_temp_max = Label(window, text=day_0_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget1_temp_max.place(x=25, y=299)
    label_forecast_widget1_temp_min = Label(window, text=day_0_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget1_temp_min.place(x=126, y=299)

    label_forecast_widget1_condition = Label(window, text=day_0_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget1_condition.place(x=30 + condition_x_0, y=265)

    label_forecast_widget1_date = Label(window, text=f_date_0, background="white", font=("bahnschrift", 13))
    label_forecast_widget1_date.place(x=52, y=110)

    label_forecast_widget1_day = Label(window, text=weekday_0, background="white", font=("bahnschrift", 13))
    label_forecast_widget1_day.place(x=60, y=135)

    # 2


    F_forecast_widget_2 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_2.place(x=200, y=107)

    canvas2 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas2.place(x=212, y=160)

    img_2 = PhotoImage(file=day_1_icon)
    canvas2.create_image(65, 50, image=img_2)

    label_forecast_widget2_temp_max = Label(window, text=day_1_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget2_temp_max.place(x=205, y=299)
    label_forecast_widget2_temp_min = Label(window, text=day_1_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget2_temp_min.place(x=306, y=299)

    label_forecast_widget2_condition = Label(window, text=day_1_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget2_condition.place(x=210 + condition_x_1, y=265)

    label_forecast_widget2_date = Label(window, text=f_date_1, background="white", font=("bahnschrift", 13))
    label_forecast_widget2_date.place(x=232, y=110)

    label_forecast_widget2_day = Label(window, text=weekday_1, background="white", font=("bahnschrift", 13))
    label_forecast_widget2_day.place(x=240, y=135)

    # Day 3

    F_forecast_widget_3 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_3.place(x=380, y=107)

    canvas3 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas3.place(x=392, y=160)

    img_3 = PhotoImage(file=day_2_icon)
    canvas3.create_image(65, 50, image=img_3)

    label_forecast_widget3_temp_max = Label(window, text=day_2_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget3_temp_max.place(x=385, y=299)
    label_forecast_widget3_temp_min = Label(window, text=day_2_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget3_temp_min.place(x=486, y=299)

    label_forecast_widget3_condition = Label(window, text=day_2_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget3_condition.place(x=390 + condition_x_2, y=265)

    label_forecast_widget3_date = Label(window, text=f_date_2, background="white", font=("bahnschrift", 13))
    label_forecast_widget3_date.place(x=412, y=110)

    label_forecast_widget3_day = Label(window, text=weekday_2, background="white", font=("bahnschrift", 13))
    label_forecast_widget3_day.place(x=420, y=135)

    # 4


    F_forecast_widget_4 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_4.place(x=560, y=107)

    canvas4 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas4.place(x=572, y=160)

    img_4 = PhotoImage(file=day_3_icon)
    canvas4.create_image(65, 50, image=img_4)

    label_forecast_widget4_temp_max = Label(window, text=day_3_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget4_temp_max.place(x=565, y=299)
    label_forecast_widget4_temp_min = Label(window, text=day_3_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget4_temp_min.place(x=666, y=299)

    label_forecast_widget4_condition = Label(window, text=day_3_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget4_condition.place(x=570 + condition_x_3, y=265)

    label_forecast_widget4_date = Label(window, text=f_date_3, background="white", font=("bahnschrift", 13))
    label_forecast_widget4_date.place(x=592, y=110)

    label_forecast_widget4_day = Label(window, text=weekday_3, background="white", font=("bahnschrift", 13))
    label_forecast_widget4_day.place(x=600, y=135)

    # 5

    F_forecast_widget_5 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_5.place(x=740, y=107)

    canvas5 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas5.place(x=752, y=160)

    img_5 = PhotoImage(file=day_4_icon)
    canvas5.create_image(65, 50, image=img_5)

    label_forecast_widget5_temp_max = Label(window, text=day_4_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget5_temp_max.place(x=745, y=299)
    label_forecast_widget5_temp_min = Label(window, text=day_4_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget5_temp_min.place(x=846, y=299)

    label_forecast_widget5_condition = Label(window, text=day_4_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget5_condition.place(x=750 + condition_x_4, y=265)

    label_forecast_widget5_date = Label(window, text=f_date_4, background="white", font=("bahnschrift", 13))
    label_forecast_widget5_date.place(x=772, y=110)

    label_forecast_widget5_day = Label(window, text=weekday_4, background="white", font=("bahnschrift", 13))
    label_forecast_widget5_day.place(x=780, y=135)

    # 6

    F_forecast_widget_6 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_6.place(x=920, y=107)

    canvas6 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas6.place(x=932, y=160)

    img_6 = PhotoImage(file=day_5_icon)
    canvas6.create_image(65, 50, image=img_6)

    label_forecast_widget6_temp_max = Label(window, text=day_5_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget6_temp_max.place(x=925, y=299)
    label_forecast_widget6_temp_min = Label(window, text=day_5_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget6_temp_min.place(x=1026, y=299)

    label_forecast_widget6_condition = Label(window, text=day_5_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget6_condition.place(x=930 + condition_x_5, y=265)

    label_forecast_widget6_date = Label(window, text=f_date_5, background="white", font=("bahnschrift", 13))
    label_forecast_widget6_date.place(x=952, y=110)

    label_forecast_widget6_day = Label(window, text=weekday_5, background="white", font=("bahnschrift", 13))
    label_forecast_widget6_day.place(x=960, y=135)

    # 7

    F_forecast_widget_7 = Frame(window, height=220, width=155, background="white", bd="3px", relief=FLAT)
    F_forecast_widget_7.place(x=1100, y=107)

    canvas7 = Canvas(window, height=100, width=130, background="white",highlightthickness=0)
    canvas7.place(x=1112, y=160)

    img_7 = PhotoImage(file=day_6_icon)
    canvas7.create_image(65, 50, image=img_7)

    label_forecast_widget7_temp_max = Label(window, text=day_6_max, background="white", font=("bahnschrift", 13))
    label_forecast_widget7_temp_max.place(x=1105, y=299)
    label_forecast_widget7_temp_min = Label(window, text=day_6_min, background="white", font=("bahnschrift", 13))
    label_forecast_widget7_temp_min.place(x=1206, y=299)

    label_forecast_widget7_condition = Label(window, text=day_6_c_f, background="white", font=("bahnschrift", 11))
    label_forecast_widget7_condition.place(x=1110 + condition_x_6, y=265)

    label_forecast_widget7_date = Label(window, text=f_date_6, background="white", font=("bahnschrift", 13))
    label_forecast_widget7_date.place(x=1132, y=110)

    label_forecast_widget7_day = Label(window, text=weekday_6, background="white", font=("bahnschrift", 13))
    label_forecast_widget7_day.place(x=1140, y=135)

    # date , day , icon , max , min

    forecast_graph_time= []
    forecast_graph_temp= []
    forecast_graph_pop= []
    forecast_graph_ws= []


    for i in all_hours:
        forecast_graph_time.append(i["datetime"][0:2])

    for i in all_hours:
        forecast_graph_temp.append(i["temp"])

    for i in all_hours:
        forecast_graph_pop.append(i["precipprob"])

    for i in all_hours:
        forecast_graph_ws.append(i["windspeed"])


    forecast_temp_graph = dict(zip(forecast_graph_time, forecast_graph_temp))

    forecast_pop_graph = dict(zip(forecast_graph_time, forecast_graph_pop))

    forecast_ws_graph = dict(zip(forecast_graph_time, forecast_graph_ws))


    def plotting():
        # the figure that will contain the plot
        fig = Figure(figsize=(15, 6),
                     dpi=95)


        y = forecast_temp_graph.values()
        x = forecast_temp_graph.keys()

        # adding the subplot
        plot1 = fig.add_subplot(211)
        plot1.set_xlim((-0.7, 24))

        plot1.set_ylim((-30, 50))

        #plot1.set_title("Per Hour Temperature")

        plot1.set_xlabel("Time of Day (Digital Time)")

        plot1.set_ylabel("Temperature ")

        loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
        plot1.xaxis.set_major_locator(loc)
        # plotting the graph

        plot1.plot(x, y, color='orange', marker='o')

        for x, y in zip(x, y):
            label = "{}".format(y)
            plot1.annotate(label, xy=(x, y), textcoords='offset points', xytext=(0, 10), ha='center')

        # creating the Tkinter canvas
        # containing the Matplotlib figure

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().place(x=-80, y=400)




    def plotting1():
        fig1 = Figure(figsize=(15, 6), dpi=95)
        y = list(forecast_pop_graph.values())
        x = list(forecast_pop_graph.keys())
        plot2 = fig1.add_subplot(211)

        plot2.set_xlim((-0.7, 24))

        plot2.set_ylim((0, 100))


        plot2.bar(x,y,color ='blue', width=0.8)

        # creating the bar plot

        plot2.set_title("Per Hour Precipitation Probability")
        plot2.set_xlabel("Time of Day (Digital Time)")
        plot2.set_ylabel("Precipitation Probability %")


        #loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
        #plot2.xaxis.set_major_locator(loc)
        for bar in plot2.patches:
            plot2.annotate(format(bar.get_height(), ''),
                           (bar.get_x() + bar.get_width() / 2,
                            bar.get_height()), ha='center', va='center',
                           size=10, xytext=(0, 8),
                           textcoords='offset points')

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas1 = FigureCanvasTkAgg(fig1, master=window)
        canvas1.draw()

        # placing the canvas on the Tkinter window
        canvas1.get_tk_widget().place(x=-80,y=400)

        # creating the Matplotlib toolba


        # the figure that will contain the plot


    #    fig1 = Figure(figsize=(5, 5),dpi=90)



    def plotting2():
        fig2 = Figure(figsize=(15, 6), dpi=95)

        y = list(forecast_ws_graph.values())
        x = list(forecast_ws_graph.keys())
        plot3 = fig2.add_subplot(211)
        plot3.set_xlim((-0.7, 24))

        plot3.set_ylim((0, 50))

        plot3.bar(x, y, color='#ADD8E6', width=0.8)
        # adding the subplot
        # creating the bar plot

       # plot3.set_title("Per Hour Wind Speed")

        plot3.set_xlabel("Time of Day (Digital Time)")

        plot3.set_ylabel("Wind speed ")

        loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
        plot3.xaxis.set_major_locator(loc)

        for bar in plot3.patches:
            plot3.annotate(format(bar.get_height(), ''),
                           (bar.get_x() + bar.get_width() / 2,
                            bar.get_height()), ha='center', va='center',
                           size=10, xytext=(0, 8),
                           textcoords='offset points')


        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas2 = FigureCanvasTkAgg(fig2, master=window)

        canvas2.draw()

        # placing the toolbar on the Tkinter window


        canvas2.get_tk_widget().place(x=-80, y=400)

        # the figure that will contain the plot


    #plotting1()


    F_filler_g = Frame (window , height  = 80, width = 1280, bg = "white").place(x=0, y = 340)



    button_label = Label(window, text="GRAPH REPRESENTING HOURLY ",width =30,bg= "white",font=("bahnschrift", 20))
    button_label.place(x=10, y =355)
    button_label_1 = Label(window, text="",bg= "white",font=("bahnschrift", 20))
    button_label_1.place(x=437, y =355)

#Image button
    img_btn = Image.open("pixel/thermometer-sun-heat-temperature-icon-vector-22773423.jpg")
    resize_img_btn = img_btn.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_btn = ImageTk.PhotoImage(resize_img_btn)

    img_btn1 = Image.open("pixel/rain.png")
    resize_img_btn1 = img_btn1.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_btn1 = ImageTk.PhotoImage(resize_img_btn1)

    img_btn2 = Image.open("pixel/168-1686015_catoon-wind-wind-swirl-clipart-removebg-preview.png")
    resize_img_btn2 = img_btn2.resize((40, 40), Image.ANTIALIAS)
    new_resized_img_btn2 = ImageTk.PhotoImage(resize_img_btn2)


    def graph_txt0():
        button_label_1.configure(text="TEMPERATURE", fg="orange")
    def graph_txt1():
        button_label_1.configure(text="PRECIPITATION PROBABILITY", fg ="blue")
    def graph_txt2():
        button_label_1.configure(text="WIND SPEED", fg="#ADD8E6")



    Button1 = Button(window, command=lambda:[graph_txt0(), plotting()], image=new_resized_img_btn)
    Button1.place(x = 1000 , y = 350)

    Button2 = Button(window, command=lambda:[graph_txt1(), plotting1()], image=new_resized_img_btn1)
    Button2.place(x = 1100 , y =350)

    Button3 = Button(window, command=lambda:[graph_txt2(), plotting2()], image=new_resized_img_btn2)
    Button3.place(x = 1200 , y =350)



    time_label_forecast = Label(window,foreground="black", background="white",font=("bahnschrift", 25))
    time_label_forecast.place(x=0,y=40)


    def refresher_forecast():
        response = requests.get("https://www.timeapi.io/api/Time/current/coordinate?latitude={}&longitude={}".format(lat, long))
        data = response.json()
        timeApi0 = data['dateTime'][11:19]
        timeApi = timeApi0.replace(":", " : ")
        dateApi = data['dateTime'][0:10]
        time_label_forecast.configure(text=timeApi)
        time_label_forecast.after(5000, refresher_forecast)
        return dateApi




    date1 = refresher_forecast()


    date_label_forecast = Label(window,foreground="black",text=date1, background="white",font=("bahnschrift", 25))
    date_label_forecast.place(x=1, y=1 )

    plotting()

    # EXIT
    img_bck1 = Image.open("pixel/bck-removebg-preview.png")
    resize_img_bck1 = img_bck1.resize((105, 84), Image.ANTIALIAS)
    new_resized_img_bck1 = ImageTk.PhotoImage(resize_img_bck1)







    btn = Button(window,image=new_resized_img_bck1,
                 command=window.destroy, relief=FLAT,background="white")  # RIDGE , GROOVE , SUNKEN
    btn.place(x =1165,y=1)



    mainloop()
