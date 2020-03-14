import RPi.GPIO as GPIO
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numberi$

class LED():
 def __init__(self, pin):
  GPIO.setup(pin, GPIO.OUT)
  self.pin = pin
  GPIO.output(self.pin, GPIO.LOW)
  self.previous_state = GPIO.LOW

 def toggle(self):
  if self.previous_state == GPIO.LOW:
   GPIO.output(self.pin, GPIO.HIGH)
   self.previous_state = GPIO.HIGH
  else:
   GPIO.output(self.pin, GPIO.LOW)
   self.previous_state = GPIO.LOW
