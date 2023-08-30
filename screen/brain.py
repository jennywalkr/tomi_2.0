import os
import sys 
import time
import logging
import random
import schedule
import requests
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime, timedelta

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
disp = LCD_2inch.LCD_2inch()

# Time stuff
currentDateAndTime = datetime.now()
currentHour = currentDateAndTime.hour
currentTime = currentDateAndTime.strftime("%H:%M")
currentDate = currentDateAndTime.strftime("%d/%m/%y")

# Fonts
timeFont = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",75)
timerFont = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",75)
dateFont = ImageFont.truetype("../Font/RobotoMono-Light.ttf",30)
RobotoMono38 = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",38)
RobotoMono28 = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",28)
RobotoMono18 = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",18)
codingFont = ImageFont.truetype("../Font/VT323-Regular.ttf",36)

# Weather info
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "3e02f2f41276ca3113c62f03973828c4"
CITY = "Sheffield"
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius = temp_kelvin - 273.15
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

disp.Init()

def blank():
    disp.clear()
    image1 = Image.new("RGB", (disp.height, disp.width ), "BLACK")
    image1=image1.rotate(180)
    disp.ShowImage(image1)
    time.sleep(5)

def clock():
    disp.clear()
    if 7 < currentHour < 21:
        x = "BLACK"
        y = "WHITE"
    else:
        x = "WHITE"
        y = "BLACK"
    image1 = Image.new("RGB", (disp.height, disp.width ), y)
    draw = ImageDraw.Draw(image1)
    draw.text((50, 50), currentTime, fill = x,font=timeFont)
    draw.text((90, 150), currentDate, fill = x,font=dateFont)
    image1=image1.rotate(180)
    disp.ShowImage(image1)
    time.sleep(30)

def weatherforecast():
    disp.clear()
    weather_icon = response['weather'][0]['icon']
    image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
    icon = Image.open("../lib/icons/" + weather_icon + ".jpg")
    back_image = image1.copy()
    back_image.paste(icon, (0,140))
    draw = ImageDraw.Draw(back_image)
    draw.text((5, 0),f"{temp_celsius:.2f}°C", fill = (225,68,0),font=RobotoMono38)
    draw.text((240, 0),f"{humidity}%", fill = (205,0,225),font=RobotoMono38)
    draw.text((105, 175),f"{sunrise_time}", fill = (230,178,0) ,font=RobotoMono18)
    draw.text((105, 200),f"{sunset_time}", fill = (255,152,51),font=RobotoMono18)
    draw.text((5, 45),"Looks like", fill = "BLACK",font=RobotoMono28)
    draw.text((5, 75),description, fill = "BLUE",font=RobotoMono28)
    draw.text((5, 105),f"in {CITY} today", fill = "BLACK",font=RobotoMono28)
    draw.text((105, 150),f"Wind speed {wind_speed}m/s",fill = (0,188,13),font=RobotoMono18)
    image1=back_image.rotate(180)
    disp.ShowImage(image1)
    time.sleep(5)

def coding():
    disp.clear()
    image1 = Image.new("RGB", (disp.height, disp.width ), "BLACK")
    draw = ImageDraw.Draw(image1)
    draw.text((0, 0), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 30), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 60), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 90), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 120), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 150), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 180), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    draw.text((0, 210), str(random.randrange(10000000000000000000000, 99999999999999999999999)), fill = (0,225,0),font=codingFont)
    image1=image1.rotate(180)
    disp.ShowImage(image1)
    time.sleep(5)

#def disco():
    #for a in [225, 225,225,0, 0, 0, 167, 255], b in [0, 158, 233, 255, 255, 0, 0, 0], c in [0, 0, 0, 0, 238, 255, 255, 240]:
    #    disp.clear()
    #    red = Image.new("RGB", (disp.height, disp.width ), (a,b,c))
    #    disp.ShowImage(red)
    #    time.sleep(0.5)
    

def countdown():
    mins = int(input("enter time in minutes: "))
    secs = mins*60
    def timer(secs):
        while secs > 0:
            time = str(timedelta(seconds = secs))
            image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
            draw = ImageDraw.Draw(image1)
            draw.text((4, 65), time, fill = "BLACK",font=timerFont)
            image1=image1.rotate(180)
            disp.ShowImage(image1)
            print(time)
            secs -= 1
    schedule.every().second.do(timer(secs))
    schedule.run_pending()

def earth():
    disp.clear()
    for x in range(1,16):
        icon = Image.open("../lib/icons/" + "frame" + str(x) + ".jpg")
        image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
        back_image = image1.copy()
        back_image.paste(icon, (50,50))
        image1=back_image.rotate(180)
        disp.ShowImage(image1)

## Testing ##
earth()
earth()
earth()
earth()
earth()
earth()
earth()
earth()
disp.module_exit()