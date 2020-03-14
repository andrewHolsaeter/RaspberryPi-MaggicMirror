import time
import RPi.GPIO as GPIO
from button import Button

def printOut(*args):
 print("Pressed")
 for arg in args:
  print("\t", arg)

btn = Button(29)
btn.subscribe(printOut, "One arg")
btn.subscribe(printOut, "Two Args", "arg2")

while(True):
 btn.read()
 time.sleep(0.2)
