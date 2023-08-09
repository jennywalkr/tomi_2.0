import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
disp = LCD_2inch.LCD_2inch()
disp.Init()
disp.clear()
draw = ImageDraw.Draw(image1)

currentDateAndTime = datetime.now()
currentHour = currentDateAndTime.hour
currentTime = currentDateAndTime.strftime("%H:%M")
currentDate = currentDateAndTime.strftime("%d/%m/%y")

image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")

timeFont = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",75)
dateFont = ImageFont.truetype("../Font/RobotoMono-Light.ttf",30)
draw.text((50, 75), currentTime, fill = "BLACK",font=timeFont)
draw.text((90, 150), currentDate, fill = "BLACK",font=dateFont)

image1=image1.rotate(180)
disp.ShowImage(image1)
time.sleep(5)
disp.module_exit()

#if currentHour > 21 or currentHour < 6:
#    x = WHITE and y = BLACK
#else:
#    x = BLACK and y = WHITE

