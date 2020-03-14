import RPi.GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

class Button():
 def __init__(self, pin, name="unknown"):
  """
  Takes a pin number and function to call on depress (currently on HIGH)
  """
  GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set input pin # and set initial value
  self.pin = pin
  self.name = name
  self.callbacks = []
  self.previous_state = GPIO.LOW
  self.button_presses = 0

 def subscribe(self, callback, *args):
  """
  Takes a function and optional args to call when btn pressed
  """
  self.callbacks.append((callback, args))

 def call(self):
  """
  Calls every callback function with args for a btn
  Callbacks should be a list of tuples w/ each instance(func, [args])
  """
  for cb in self.callbacks:
   if len(cb[1]) > 0:
    cb[0](*cb[1])
   else:
    cb[0]()

 def read(self):
  state = GPIO.input(self.pin)

  if (state != self.previous_state):
   # Update state here so callback functions can access "current state"
   self.previous_state = state
   if (state == GPIO.LOW):
    self.button_presses +=1
    self.call()
