import time
import RPi.GPIO as GPIO
from button import Button
from led import LED

def printState(btn):
 print("{} pressed {} times".format(btn.name, btn.button_presses))

def toggleLED(led):
 led.toggle()

btnGreen = Button(29, "Green")
btnRed = Button(31, "Red")
btns = [btnGreen, btnRed]

ledGreen = LED(11)
ledRed = LED(13)

btnGreen.subscribe(toggleLED, ledGreen)
btnRed.subscribe(toggleLED, ledRed)

btnGreen.subscribe(printState, btnGreen)
btnRed.subscribe(printState, btnRed)

while(True):
 for btn in btns:
  btn.read()
 time.sleep(0.2)
