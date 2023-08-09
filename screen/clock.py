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

currentDateAndTime = datetime.now()
currentHour = currentDateAndTime.hour
currentTime = currentDateAndTime.strftime("%H:%M")
currentDate = currentDateAndTime.strftime("%d/%m/%y")

if currentHour > 21 or currentHour < 6:
    x = WHITE and y = BLACK
else:
    x = BLACK and y = WHITE

image1 = Image.new("RGB", (disp.height, disp.width ), "y")

timeFont = ImageFont.truetype("../Font/RobotoMono-Regular.ttf",35)
dateFont = ImageFont.truetype("../Font/Roboto-Regular",20)
draw.text((50, 50), currentTime, fill = "x",font=timeFont)
draw.text((100, 175), currentDate, fill = "x",font=dateFont)

image1=image1.rotate(180)
disp.ShowImage(image1)
time.sleep(5)
disp.module_exit()

