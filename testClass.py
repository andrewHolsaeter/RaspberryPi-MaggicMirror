import time
import subprocess
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
 #os.system("python3 hello.py")
 #print("{} pressed {} times".format(btn.name, btn.button_presses))

def toggleLED(led):
 led.toggle()

btnGreen = Button(29, "Green")
btnRed = Button(31, "Red")
btns = [btnGreen, btnRed]

ledGreen = LED(11)
ledRed = LED(13)

btnGreen.subscribe(toggleLED, ledGreen)
btnGreen.subscribe(toggleMirror, ledGreen)

btnRed.subscribe(toggleLED, ledRed)
btnRed.subscribe(printState, btnRed, ledRed)

while(True):
 for btn in btns:
  btn.read()
 time.sleep(0.2)
