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


def blank():
    disp.Init()
    disp.clear()
    image1 = Image.new("RGB", (disp.height, disp.width ), "BLACK")
    image1=image1.rotate(180)
    disp.ShowImage(image1)
    time.sleep(5)
    disp.module_exit()

