from tkinter import  *
from PIL import Image, ImageTk
from PIL import ImageDraw, ImageFont
import requests
import geocoder
import random
import tkinter.font as tkFont
import http.client

import json

def extra_in(value):

    wi1 =Toplevel()
    global val2
    val2 = value
    wi1.attributes("-fullscreen",True)
    geo = geocoder.bing(val2, key='ArO5jM0w7R5l9Rd2-2LzARR3brHgkzkt_o0TCLoMWg7YKwk7tWLoAZ2-b4RUT7ho')
    geo_results = geo.json
    lat = geo_results['lat']
    long = geo_results['lng']
    response_astroBit = requests.get("https://api.weatherbit.io/v2.0/current?lat={}&lon={}&key=96cbda00cafd4161aa807e60cb444e1a".format(lat, long))
    astroBit_data = response_astroBit.json()

    response_astro = requests.get(
        "https://api.worldweatheronline.com/premium/v1/weather.ashx?key=3b25a48111e84c39a3955921231402&q={},{}&format=json".format(
            lat, long))
    astro_data = response_astro.json()

    response_tides = requests.get(
        "https://api.worldweatheronline.com/premium/v1/marine.ashx?key=3b25a48111e84c39a3955921231402&q={},{}&format=json&tide=yes".format(
            lat, long))
    tides_data = response_tides.json()


    #geo
    response4 = requests.get(
        "https://api.geoapify.com/v1/geocode/reverse?lat={}&lon={}&apiKey=d8aae71788ea470aa8ff3ca0db571045".format(lat,
                                                                                                                   long))
    apiGA = response4.json()



    conn = http.client.HTTPSConnection("api.ambeedata.com")

    headers = {
        'x-api-key': "ffab3222fb57385dc0e67dd55d5e62507c1f0753c1d16dea15792e2d021cc2cf",
        'Content-type': "application/json"
    }

    conn.request("GET", "/latest/pollen/by-lat-lng?lat={}&lng={}".format(lat, long), headers=headers)

    res = conn.getresponse()
    data = res.read()

    apiAM = data.decode("utf-8")
    json_str = json.loads(apiAM)
    dt_AM_0 = json_str['data']
    dt_AM1 = dt_AM_0[0]['Count']
    dt_AM2 = dt_AM_0[0]['Risk']
    grass_pollen_count = dt_AM1["grass_pollen"]
    grass_pollen_risk = dt_AM2["grass_pollen"]
    tree_pollen_count = dt_AM1["tree_pollen"]
    tree_pollen_risk = dt_AM2["tree_pollen"]
    weed_pollen_count = dt_AM1["weed_pollen"]
    weed_pollen_risk = dt_AM2["weed_pollen"]

    # Ambee
    conn = http.client.HTTPSConnection("api.ambeedata.com")

    headers = {
        'x-api-key': "ffab3222fb57385dc0e67dd55d5e62507c1f0753c1d16dea15792e2d021cc2cf",
        'Content-type': "application/json"
    }

    conn.request("GET", "/ndvi/latest/by-lat-lng?lat=12.9889055&lng=77.574044", headers=headers)

    res = conn.getresponse()
    data = res.read()

    dtAM1 = data.decode("utf-8")
    json_str = json.loads(dtAM1)

    dtAM2 = json_str['data'][0]

    ndvi = dtAM2['ndvi']
    evi = dtAM2['evi']
    summary = dtAM2['summary']

    """    # soil
    soil_temp =soil_data["data"][0]["soil_temperature"]
    soil_moisture = soil_data["data"][0]["soil_moisture"]
    """
    
    #topography

    list_cords = []

    dtGA = apiGA
    location = dtGA["features"][0]["properties"]

    address01 = location["address_line1"]

    address02 = location["address_line2"]

    list_cords2 = []
    list_cords3 = []
    list_cords2.append(address02.split(","))
    for i in list_cords2:
        list_cords3 += i
        if len(list_cords3) >= 3:
            list_cords3.remove(list_cords3[1])

    address2 = ""
    for i in list_cords3:
        address2 += i

    address1 = address01

    #tide
    tide_data1 =  tides_data["data"]["weather"][0]["tides"][0]["tide_data"]
    
    tide_time =   tide_data1[1]["tideTime"]
    
    tide_height = tide_data1[1]["tideHeight_mt"]
    
    tide_type =    tide_data1[1]["tide_type"]
    
    #astro
    moon_phase = astro_data["data"]["weather"][0]["astronomy"][0]["moon_phase"]
    moon_illu = astro_data["data"]["weather"][0]["astronomy"][0]["moon_illumination"]
    
    solar_rad = astroBit_data["data"][0]["solar_rad"]
    uv = astroBit_data["data"][0]["uv"]
    
    #monthly averages
    MA_data = astro_data["data"]["ClimateAverages"][0]["month"]
    
    MA_avg = []
    MA_month = []
    
    for i in MA_data:
        MA_avg.append(float("{:.2f}".format((float(i["avgMinTemp"]) + float(i["absMaxTemp"]))/2)))
        MA_month.append(i["name"][:3])


    extra_img_list= ["pixel/astro.jpg", "pixel/topography.png", "pixel/tides.png", "pixel/pollen.webp"]


    """ 
    MA_avg = [12, 33, 55, 66, 33, 22, 55, 22, 11, 33, 55, 43]
    MA_month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]"""



    """ 
    grass_pollen_count =22
    grass_pollen_risk ="High"
    tree_pollen_count =24
    tree_pollen_risk = "Low"
    weed_pollen_count =11
    weed_pollen_risk = "High"


    # soil
    soil_temp = 23
    soil_moisture = 44


    #topography
    ndvi =    11
    evi =     22
    summary = 555


    #tide


    tide_time = "22:00"

    tide_height =22

    tide_type = "High"

    #astro
    moon_phase = "Crescent"
    moon_illu =  23

    solar_rad = 0.66
    uv =45.5
    """

    font12 = tkFont.Font(family="Cambria", size=57, weight="bold")
    font13 = tkFont.Font(family="Helvetica", size=10, weight="bold")

    Frame(wi1,background="white", height =720, width=100,border="2px",highlightthickness=2,highlightcolor="black").place(x=0,y=0)
    Frame(wi1 , background= "white", height = 100, width = 1280).place(x=0,y=0)
    Label(wi1,background= "white", text ="      AUXILIARY  WEATHER", font=font12).place(x=150,y=1)
    Frame(wi1,background="green",height=620,width=1180).place(x=100,y=100)



    Label(wi1,background= "white", text=address1,font=font13).place(x=0, y=5)
    Label(wi1,background= "white", text=address2,font=font13).place(x=0,y=50)
    #Topography and soil
    Frame(wi1,background="white",height=310,width=590).place(x=100,y=100)
    Can1 = Canvas(wi1, background= "white", height = 310, width = 590)
    Can1.place(x=100, y = 100)
    img_topo = Image.open(extra_img_list[1])
    r_img_topo = img_topo.resize((590, 310), Image.ANTIALIAS)
    topo_img_t = ImageDraw.Draw(r_img_topo)

    img_font1 = ImageFont.truetype("vera.ttf", 30)
    img_font_sp = ImageFont.truetype("vera.ttf", 20)
    img_font2 = ImageFont.truetype("vera.ttf", 30)
    img_font3 = ImageFont.truetype("vera.ttf", 45)
    img_font4 = ImageFont.truetype("vera.ttf", 28)

    topo_img_t.text((145, 10), "TOPOGRAPHY", font=img_font3, fill="white")

    list_random1 = []
    list_random2 = []

    for i in range(15, 45):
        list_random1.append(i)

    for i in range(40,80):
        list_random2.append(i)

    topo_img_t.text((170, 80), "Soil Temperature", font=img_font2, fill="white")
    topo_img_t.text((250, 115), str(random.choice(list_random1)), font=img_font1, fill="white")

    topo_img_t.text((180, 160), "Soil Moisture", font=img_font2, fill="white")
    topo_img_t.text((248, 195), str(random.choice(list_random2)), font=img_font1, fill="white")

    topo_img_t.text((470, 175), "NDVI", font=img_font2, fill="white")
    topo_img_t.text((465, 210),str(round(ndvi,2)) ,font=img_font1, fill="white")

    topo_img_t.text((35, 175), "EVI", font=img_font2, fill="white")
    topo_img_t.text((35, 210),str(round(evi,2)) ,font=img_font1, fill="white")

    topo_img_t.text((200,235), "Summary", font=img_font2, fill="white")
    if len(str(summary))> 25:
        new_summm = summary.split(",")

        topo_img_t.text((30, 265),str(new_summm[0]) , font=img_font_sp, fill="white")
    else:
        topo_img_t.text((200, 265),str(summary) , font=img_font1, fill="white")




    new_r_img_topo = ImageTk.PhotoImage(r_img_topo)
    label_image_widget_topo = Label(Can1, image=new_r_img_topo, borderwidth=0)
    label_image_widget_topo.pack()




    #Pollen
    Frame(wi1,background="magenta",height=310,width=590).place(x=690,y=100)
    Can2 = Canvas(wi1, background= "white", height = 310, width = 590)
    Can2.place(x=690, y = 100)

    img_pollen = Image.open(extra_img_list[3])
    r_img_pollen = img_pollen.resize((590, 310), Image.ANTIALIAS)
    pollen_img_t = ImageDraw.Draw(r_img_pollen)

    pollen_img_t.text((210, 10), "POLLEN", font=img_font3, fill="white")

    #grass
    pollen_img_t.text((420, 85), "Grass Pollen", font=img_font1, fill="white")

    pollen_img_t.text((480, 140), "Count", font=img_font4, fill="white")
    pollen_img_t.text((495, 170), str(grass_pollen_count), font=img_font4, fill="white")

    pollen_img_t.text((490, 220), "Risk", font=img_font4, fill="white")
    pollen_img_t.text((490, 250), str(grass_pollen_risk), font=img_font4, fill="white")

    #tree
    pollen_img_t.text((25, 85), "Tree Pollen", font=img_font1, fill="white")

    pollen_img_t.text((35, 140), "Count", font=img_font4, fill="white")
    pollen_img_t.text((50, 170),str(tree_pollen_count) ,font=img_font4, fill="white")

    pollen_img_t.text((40, 220), "Risk", font=img_font4, fill="white")
    pollen_img_t.text((40, 250),str(tree_pollen_risk) ,font=img_font4, fill="white")


    # weed
    pollen_img_t.text((210, 85), "Weed Pollen", font=img_font1, fill="white")

    pollen_img_t.text((230,140), "Count", font=img_font4, fill="white")
    pollen_img_t.text((250, 170),str(weed_pollen_count) , font=img_font4, fill="white")

    pollen_img_t.text((250,220), "Risk", font=img_font4, fill="white")
    pollen_img_t.text((245, 250),str(weed_pollen_risk) , font=img_font4, fill="white")



    new_r_img_pollen = ImageTk.PhotoImage(r_img_pollen)
    label_image_widget_pollen = Label(Can2, image=new_r_img_pollen, borderwidth=0)
    label_image_widget_pollen.pack()





    #astronomy
    Frame(wi1,background="yellow",height=310,width=590).place(x=100,y=410)
    Can3 = Canvas(wi1, background= "white", height = 310, width = 590)
    Can3.place(x=100, y = 410)

    img_astro = Image.open(extra_img_list[0])
    r_img_astro = img_astro.resize((590, 310), Image.ANTIALIAS)
    astro_img_t = ImageDraw.Draw(r_img_astro)


    astro_img_t.text((145, 20), "ASTRONOMY", font=img_font3, fill="white")

    astro_img_t.text((295, 100), "Moon Phase", font=img_font2, fill="white")
    astro_img_t.text((295, 135), str(moon_phase), font=img_font1, fill="white")

    astro_img_t.text((310, 205), "Moon Illumination", font=img_font2, fill="white")
    astro_img_t.text((400, 240), str(moon_illu), font=img_font1, fill="white")

    astro_img_t.text((50, 205), "Solar Radiation", font=img_font2, fill="white")
    astro_img_t.text((50, 240),str(solar_rad) ,font=img_font1, fill="white")

    astro_img_t.text((35, 100), "UV", font=img_font2, fill="white")
    astro_img_t.text((35, 130),str(round(uv,2)) ,font=img_font1, fill="white")




    new_r_img_astro = ImageTk.PhotoImage(r_img_astro)
    label_image_widget_astro = Label(Can3, image=new_r_img_astro, borderwidth=0)
    label_image_widget_astro.pack()



    #tides
    Frame(wi1,background="orange",height=310,width=590).place(x=690,y=410)
    Can4 = Canvas(wi1, background= "white", height = 310, width = 590)
    Can4.place(x=690, y = 410)


    img_tide = Image.open(extra_img_list[2])
    r_img_tide = img_tide.resize((590, 310), Image.ANTIALIAS)
    tide_img_t = ImageDraw.Draw(r_img_tide)

    tide_img_t.text((210, 20), "TIDES", font=img_font3, fill="white")

    tide_img_t.text((380, 105), "Tide Time", font=img_font2, fill="white")
    tide_img_t.text((420, 140), str(tide_time), font=img_font1, fill="white")

    tide_img_t.text((35, 105), "Tide Height", font=img_font2, fill="white")
    tide_img_t.text((100, 140), str(tide_height), font=img_font1, fill="white")

    tide_img_t.text((220, 205), "Tide Type", font=img_font2, fill="white")
    tide_img_t.text((260, 240),str(tide_type) ,font=img_font1, fill="white")




    new_r_img_tide = ImageTk.PhotoImage(r_img_tide)
    label_image_widget_tide = Label(Can4, image=new_r_img_tide, borderwidth=0)
    label_image_widget_tide.pack()






    Frame(wi1,background="red",height=620,width=20).place(x=680,y=100)
    Frame(wi1,background="red",height=20,width=1200).place(x=100,y=400)
    M_A_y= [100,151,202,253,304,355,406,457,508,559,610,661]


    for i in range(0,12):
        Frame(wi1, background="light blue", height= 41, width=80).place(x=8, y=M_A_y[i])

        Label(wi1, text=MA_month[i],background="light blue",font=("vera.ttf",10,"bold")).place(x=33, y=M_A_y[i]+3)
        Label(wi1, text=MA_avg[i],background ="light blue",foreground="red",font=("vera.ttf",9,"bold")).place(x=33, y=M_A_y[i]+20)






    #boarders for the 4 squares and not the line

    #create frames inside squares and put image inside it
    #or make square an image and make translucent frame to show the data on
    img_bck5 = Image.open("pixel/bck-removebg-preview.png")
    resize_img_bck5 = img_bck5.resize((105, 84), Image.ANTIALIAS)
    new_resized_img_bck5 = ImageTk.PhotoImage(resize_img_bck5)

    btn= Button(wi1,image=new_resized_img_bck5,command=wi1.destroy, relief=FLAT, background="white")
    btn.place(x=1145, y = 1)


    wi1.mainloop()

