#!/usr/bin/env python3

import sys
import time
import subprocess
import signal
import RPi.GPIO as GPIO
from button import Button
from led import LED
from playerCopy import SpotifyPlayer

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
 state = led.previous_state
 if state == GPIO.HIGH:
  # LED
  print(led.name, "on")
 else:
  print(led.name, "off")

def toggleLED(led):
 led.toggle()

def toggleSpotifyPlayer(player, led):
 player.toggle()
 if player.status == "playing":
  led.turn_on()
 elif player.status == "paused":
  led.turn_off()
 else:
  led.blink(0.5, 3)

def shutdown(*args):
 print("Shutting down...", args)
 for led in leds:
  led.turn_off()
 sys.exit(0)

def loop():
 print("Starting up app..")

 while(True):
  for btn in btns:
   btn.read()

  time.sleep(0.2)

spotifyPlayer = SpotifyPlayer()

discoverWeekly = "37i9dQZEVXcFDmNVmwGjZd"

btnYellow = Button(29, "Yellow")
btnRed = Button(31, "Red")
btns = [btnYellow, btnRed]

ledGreen = LED(11, "Green")
ledYellow = LED(13, "Yellow")
ledRed = LED(15, "Red")
leds = [ledGreen, ledYellow, ledRed]

btnYellow.subscribe(toggleLED, ledYellow)
btnYellow.subscribe(toggleMirror, ledYellow)

btnRed.subscribe(printState, btnRed, ledRed)
btnRed.subscribe(toggleSpotifyPlayer, spotifyPlayer, ledRed)

if __name__ == '__main__':
 # Turn on LED to show we are running
 ledGreen.turn_on()
 # Register led turn off at exit to show we aren't running
 # SIGTERM = when killed? SIGINT is sent when ctrl-c is pressed
 signal.signal(signal.SIGTERM, shutdown)
 signal.signal(signal.SIGINT, shutdown)

 loop()
