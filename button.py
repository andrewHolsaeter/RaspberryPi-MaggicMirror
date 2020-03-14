import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

class Button():
 def __init__(self, pin, callback):
  """
  Takes a pin number and function to call on depress (currently on HIGH)
  """
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set input pin # and set initial value
  self.pin = pin
  self.callback = callback
  self.previous_state = GPIO.LOW

 def call(self):
  self.callback()

 def read(self):
  state = GPIO.input(self.pin)

  if (state != self.previous_state):
   if (state == GPIO.HIGH):
    self.call()
   self.previous_state == state
