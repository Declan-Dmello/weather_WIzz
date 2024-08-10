from tkinter import *
from data_wiki import *
from PIL import ImageTk, Image
def weather_rec():
    win3 = Toplevel()
    win3.attributes('-fullscreen', True)

    Frame(win3,height =  110, width =1280,background= "white").place(x=0, y =0)
    Label(win3, text="  WEATHER    RECORDS",background="white",font=("vera.ttf",60,"bold")).place(x=120,y=5)


    def hottest_history():
        Frame(win3,height =  80, width =1280,background= "red").place(x=0, y =110)
        Label(win3,text="HIGHEST RECORDED TEMPERATURES",background="red",font=("vera.ttf",30,"bold")).place(x=270, y = 125)

    #table
        Frame(win3,height =  530, width =910,background= "white", highlightbackground="black", highlightthickness=2).place(x=0, y =190)

        y_hot= [250,310,370,430,490,550,610,670]

        canvas_0=Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_0.place(x=225, y=y_hot[0])
        img_0 = PhotoImage(file=hottest_flag[0])
        canvas_0.create_image(25, 25, image=img_0)

        canvas_1 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_1.place(x=225, y=y_hot[1])
        img_1 = PhotoImage(file=hottest_flag[1])
        canvas_1.create_image(25, 25, image=img_1)

        canvas_2 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_2.place(x=225, y=y_hot[2])
        img_2 = PhotoImage(file=hottest_flag[2])
        canvas_2.create_image(25, 25, image=img_2)

        canvas_3 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_3.place(x=225, y=y_hot[3])
        img_3 = PhotoImage(file=hottest_flag[3])
        canvas_3.create_image(25, 25, image=img_3)

        canvas_4 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_4.place(x=225, y=y_hot[4])
        img_4 = PhotoImage(file=hottest_flag[4])
        canvas_4.create_image(25, 25, image=img_4)

        canvas_5 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_5.place(x=225, y=y_hot[5])
        img_5 = PhotoImage(file=hottest_flag[5])
        canvas_5.create_image(25, 25, image=img_5)

        canvas_6 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_6.place(x=225, y=y_hot[6])
        img_6 = PhotoImage(file=hottest_flag[6])
        canvas_6.create_image(25, 25, image=img_6)

        canvas_7 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_7.place(x=225, y=y_hot[7])
        img_7 = PhotoImage(file=hottest_flag[7])
        canvas_7.create_image(25, 25, image=img_7)

        Frame(win3,background = "white", height =230 , width =370 ).place(x=911, y=501)
        Label(win3,background = "white", text="HIGHEST TEMPERATURE RECORDED ", font= ("vera.ttf",12,"bold")).place(x=915, y = 530)
        Label(win3,background = "white", text="In India : 51.0°C in Rajasthan on 19 May 2016", font= ("vera.ttf",12,"bold")).place(x=915, y = 570)
        Label(win3,background = "white", text="In Goa : 37.1°C in Panaji on 28 May 1973", font= ("vera.ttf",12,"bold")).place(x=915, y = 600)
        Label(win3,background = "white", text="WARMEST YEAR RECORDED ", font= ("vera.ttf",12,"bold")).place(x=915, y = 650)
        Label(win3,background = "white", text="2020  with  14.9°C", font= ("vera.ttf",12,"bold")).place(x=915, y = 680)

        Frame(win3, height=250, width=370, background="magenta").place(x=911, y=250)
        img_heat1 = Image.open("pixel/Koppen-Geiger_Map_B_present.svg-removebg-preview.png")
        resize_img_heat1 = img_heat1.resize((370, 250), Image.ANTIALIAS)
        new_resized_img_heat1 = ImageTk.PhotoImage(resize_img_heat1)
        Label(win3,background = "white", image = new_resized_img_heat1 ).place(x=911, y=250)

        #lines for table

        #date
        Frame(win3,height =  530, width =2,background= "black").place(x=770, y =190)
        #location
        Frame(win3,height =  530, width =2,background= "black").place(x=390, y =190)
        #country
        Frame(win3,height =  530, width =2,background= "black").place(x=280, y =190)
        #flag line just for reference remove later
        #Frame(win3,height =  530, width =2,background= "blue").place(x=50, y =190)

        #horizontal line
        Frame(win3,height =  2, width =910,background= "black").place(x=0, y =250)

        Label(win3,text="Country",background="white",font=('vera.ttf', 25, "bold")).place(x=30, y = 200)

        Label(win3,text="Temp",background="white",font=('vera.ttf', 25, "bold")).place(x=290, y = 200)
        Label(win3,text="Location",background="white",font=('vera.ttf', 25, "bold")).place(x=470, y = 200)
        Label(win3,text="Date",background="white",font=('vera.ttf', 25, "bold")).place(x=780, y = 200)


        y=260
        for i in hottest_country_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=10, y =y)
            y=y+60

        y1=260
        for i in hottest_temp_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=290, y =y1)
            y1=y1+60

        y2=260
        for i in hottest_location_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=400, y =y2)
            y2=y2+60


        y3=260
        for i in hottest_date_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=780, y =y3)
            y3=y3+60
        mainloop()



    def cold_history():

        Frame(win3, height=80, width=1280, background="light blue").place(x=0, y=110)
        Label(win3,text="LOWEST RECORDED TEMPERATURES ",background="light blue",font=("vera.ttf",30,"bold")).place(x=270, y = 125)


        #table
        Frame(win3,height =  530, width =910,background= "white", highlightbackground="black", highlightthickness=2).place(x=0, y =190)

        #lines for table

        #date
        Frame(win3,height =  530, width =2,background= "black").place(x=770, y =190)
        #location
        Frame(win3,height =  530, width =2,background= "black").place(x=390, y =190)
        #country
        Frame(win3,height =  530, width =2,background= "black").place(x=280, y =190)
        #flag line just for reference remove later
        #Frame(win3,height =  530, width =2,background= "blue").place(x=50, y =190)

        y_hot = [250, 310, 370, 430, 490, 550, 610, 670]

        canvas_0 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_0.place(x=225, y=y_hot[0])
        img_0 = PhotoImage(file=coldest_flag[0])
        canvas_0.create_image(25, 25, image=img_0)

        canvas_1 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_1.place(x=225, y=y_hot[1])
        img_1 = PhotoImage(file=coldest_flag[1])
        canvas_1.create_image(25, 25, image=img_1)

        canvas_2 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_2.place(x=225, y=y_hot[2])
        img_2 = PhotoImage(file=coldest_flag[2])
        canvas_2.create_image(25, 25, image=img_2)

        canvas_3 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_3.place(x=225, y=y_hot[3])
        img_3 = PhotoImage(file=coldest_flag[3])
        canvas_3.create_image(25, 25, image=img_3)

        canvas_4 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_4.place(x=225, y=y_hot[4])
        img_4 = PhotoImage(file=coldest_flag[4])
        canvas_4.create_image(25, 25, image=img_4)

        canvas_5 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_5.place(x=225, y=y_hot[5])
        img_5 = PhotoImage(file=coldest_flag[5])
        canvas_5.create_image(25, 25, image=img_5)

        canvas_6 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_6.place(x=225, y=y_hot[6])
        img_6 = PhotoImage(file=coldest_flag[6])
        canvas_6.create_image(25, 25, image=img_6)

        canvas_7 = Canvas(win3, height=40, width=50, background="white", highlightthickness=0)
        canvas_7.place(x=225, y=y_hot[7])
        img_7 = PhotoImage(file=coldest_flag[7])
        canvas_7.create_image(25, 25, image=img_7)

        Frame(win3, height=250, width=370, background="magenta").place(x=911, y=250)
        img_cold1 = Image.open("pixel/202107_Percent_of_global_area_at_temperature_records_-_Global_warming_-_NOAA.svg (1).png")
        resize_img_cold1 = img_cold1.resize((370, 250), Image.ANTIALIAS)
        new_resized_img_cold1 = ImageTk.PhotoImage(resize_img_cold1)
        Label(win3, background="white", image=new_resized_img_cold1).place(x=911, y=250)

        Frame(win3, background="white", height=230, width=370).place(x=911, y=501)
        Label(win3, background="white", text="LOWEST TEMPERATURE RECORDED ", font=("vera.ttf", 12, "bold")).place(x=915, y=530)
        Label(win3, background="white", text="In India : -45.8°C in Kargil,J&K on 9 Jan 1995",font=("vera.ttf", 12, "bold")).place(x=915, y=570)
        Label(win3, background="white", text="In Goa : 14.4°C in Panaji on 26 Jan 1955",font=("vera.ttf", 12, "bold")).place(x=915, y=600)
        Label(win3, background="white", text="COLDEST YEAR RECORDED ", font=("vera.ttf", 12, "bold")).place(x=915,y=650)
        Label(win3, background="white", text="1904  with  13.7°C", font=("vera.ttf", 12, "bold")).place(x=915, y=680)

        #horizontal line
        Frame(win3,height =  2, width =910,background= "black").place(x=0, y =250)

        Label(win3,text="Country",background="white",font=('vera.ttf', 25, "bold")).place(x=30, y = 200)

        Label(win3,text="Temp",background="white",font=('vera.ttf', 25, "bold")).place(x=290, y = 200)
        Label(win3,text="Location",background="white",font=('vera.ttf', 25, "bold")).place(x=470, y = 200)
        Label(win3,text="Date",background="white",font=('vera.ttf', 25, "bold")).place(x=780, y = 200)


        y=260
        for i in coldest_country_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=10, y =y)
            y=y+60

        y1=260
        for i in coldest_temp_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=300, y =y1)
            y1=y1+60

        y2=260
        for i in coldest_location_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=400, y =y2)
            y2=y2+60


        y3=260

        for i in coldest_date_list:
            Label(win3, text=i,background="white",font=('vera.ttf',14, "bold")).place(x=780, y =y3)
            y3=y3+60


        mainloop()

    img_heat1_btn = Image.open("pixel/thermometer-sun-heat-temperature-icon-vector-22773423.jpg")
    resize_img_heat1_btn = img_heat1_btn.resize((45, 45), Image.ANTIALIAS)
    new_resized_img_heat1_btn = ImageTk.PhotoImage(resize_img_heat1_btn)

    img_cold1_btn = Image.open("pixel/157-1575741_snow-snowflake-cartoon-removebg-preview.png")
    resize_img_cold1_btn = img_cold1_btn.resize((45, 45), Image.ANTIALIAS)
    new_resized_img_cold1_btn = ImageTk.PhotoImage(resize_img_cold1_btn)

    img_exit1 = Image.open("pixel/bck-removebg-preview.png")
    resize_img_exit1 = img_exit1.resize((105, 85), Image.ANTIALIAS)
    new_resized_img_exit1 = ImageTk.PhotoImage(resize_img_exit1)
    Frame(win3, background="white",height=100, width=450).place(x=910, y =160)

    Button(win3,image=new_resized_img_heat1_btn, command=hottest_history,relief=FLAT, background="white").place(x=1050,y=190)
    Button(win3, image=new_resized_img_cold1_btn, command=cold_history,relief=FLAT, background="white").place(x=1150,y=190)
    Button(win3, image=new_resized_img_exit1, command=win3.destroy,relief=FLAT, background="white").place(x=1150,y=3)

    hottest_history()
    win3.mainloop()

