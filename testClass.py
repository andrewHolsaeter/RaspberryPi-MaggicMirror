import time
import RPi.GPIO as GPIO
from button import Button

def printState(btn):
 print(btn.button_presses)

btn = Button(29)
btn.subscribe(printState, btn)

while(True):
 btn.read()
 time.sleep(0.2)
