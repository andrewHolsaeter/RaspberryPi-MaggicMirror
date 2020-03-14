import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(11, GPIO.OUT)

while True: # Run forever
    if GPIO.input(29) == GPIO.HIGH:
	GPIO.output(11, GPIO.HIGH)
        print("Button was pushed!")
    else:
	GPIO.output(11, GPIO.LOW)

    time.sleep(0.1)
