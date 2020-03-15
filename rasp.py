#!/usr/bin/env python3

import time
import subprocess
import atexit
import RPi.GPIO as GPIO
from button import Button
from led import LED

def toggleMirror(led):
 # previous state is technically current state here
 state = led.previous_state
 if state == GPIO.HIGH:
  print("Starting mirror")
  subprocess.run(['/home/pi/mmhelper.sh', 'start'])
 else:
  print("Stopping mirror")
  subprocess.run(['/home/pi/mmhelper.sh', 'stop'])

def printState(btn, led):
 # previous state is technically current state here
 state = btn.previous_state
 if state == GPIO.HIGH:
  # LED
  print("High")
 else:
  print("Low")

def toggleLED(led):
 led.toggle()

btnYellow = Button(29, "Yellow")
btnRed = Button(31, "Red")
btns = [btnYellow, btnRed]

ledGreen = LED(11)
ledYellow = LED(13)
ledRed = LED(15)
leds = [ledGreen, ledYellow, ledRed]

btnYellow.subscribe(toggleLED, ledYellow)
btnYellow.subscribe(toggleMirror, ledYellow)

btnRed.subscribe(toggleLED, ledRed)
btnRed.subscribe(printState, btnRed, ledRed)

print("Starting up app..")

# Turn on LED to show we are running
ledGreen.turn_on()
# Register led turn off at exit to show we aren't running
atexit.register(ledGreen.turn_off

while(True):
 for btn in btns:
  btn.read()
 time.sleep(0.2)
