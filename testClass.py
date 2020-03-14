import time
import RPi.GPIO as GPIO
from button import Button

def printOut():
 print("Pressed")

btn = Button(29, printOut)

while(True):
 btn.read()
 time.sleep(0.1)
