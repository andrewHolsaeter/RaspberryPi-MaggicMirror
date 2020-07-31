import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numberi$

class LED():
 def __init__(self, pin, name="unknown"):
  GPIO.setup(pin, GPIO.OUT)
  self.pin = pin
  self.name = name
  GPIO.output(self.pin, GPIO.LOW)
  self.previous_state = GPIO.LOW

 def turn_on(self):
  GPIO.output(self.pin, GPIO.HIGH)
  self.previous_state = GPIO.HIGH

 def turn_off(self):
  GPIO.output(self.pin, GPIO.LOW)
  GPIO.previous_state = GPIO.LOW

 def blink(self, speed, times):
  interval = speed / 2
  start = time.time()

  for i in range(times):
   self.turn_on()
   time.sleep(interval)
   self.turn_off()
   time.sleep(interval)

 def toggle(self):
  if self.previous_state == GPIO.LOW:
   GPIO.output(self.pin, GPIO.HIGH)
   self.previous_state = GPIO.HIGH
  else:
   GPIO.output(self.pin, GPIO.LOW)
   self.previous_state = GPIO.LOW
