import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_2inch
from PIL import Image,ImageDraw,ImageFont

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

print(disp.height)
print(disp.width)

image1 = Image.new("RGB", (disp.height, disp.width ), "WHITE")
draw = ImageDraw.Draw(image1)

draw.rectangle((0,0,15,15), fill = "BLACK")

disp.ShowImage(image1)
time.sleep(5)
disp.module_exit()

disp.module_exit()
