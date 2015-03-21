# Sarah Withee
# Intro to Hacking with the Raspberry Pi
# 3/20/2015
# Project 1 - LEDs


import time
import RPi.GPIO as GPIO

# Array of GPIO pins
pins = [3, 5, 7, 29, 31, 26, 24, 21]
# Speed between lights
speed = .2

# Set to board pin # mode
GPIO.setmode(GPIO.BOARD)

# Loop through each pin
# Set it up, then set it's output to false (off)
for i in pins:
	print("Setup: " + str(i))
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, False)


# print() statements are for debugging. Uncomment if you want them

# Loop forever. (The Cyclons never die!)
while True:
	# Go forward
  for i in range(len(pins)-1):
		#print("On: " + str(i) + " - " + str(pins[i]))
		GPIO.output(pins[i], True)
		time.sleep(speed)
		#print("Off: " + str(i) + " - " + str(pins[i]))
		GPIO.output(pins[i], False)
  # Go backward
	for i in range(len(pins)-1, 0, -1):
		#print("On: " + str(i) + " - " + str(pins[i]))
		GPIO.output(pins[i], True)
		time.sleep(speed)
		#print("Off: " + str(i) + " - " + str(pins[i]))
		GPIO.output(pins[i], False)
