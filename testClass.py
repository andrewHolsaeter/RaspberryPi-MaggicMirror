import time
import RPi.GPIO as GPIO
from button import Button
from led import LED

def printState(btn):
 print(btn.button_presses)

def toggleLED(led):
 led.toggle()

btn = Button(29)
led = LED(11)

btn.subscribe(toggleLED, led)
btn.subscribe(printState, btn)

while(True):
 btn.read()
 time.sleep(0.2)
