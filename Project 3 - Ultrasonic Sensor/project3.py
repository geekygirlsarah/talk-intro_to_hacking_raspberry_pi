# Sarah Withee
# Intro to Hacking with the Raspberry Pi
# 3/20/2015
# Project 3 - Ultrasonic sensors

import time
import RPi.GPIO as GPIO


# Set up the ultrasonic sensor pins
u1Trig = 11
u1Echo = 13
u2Trig = 19
u2Echo = 21
u3Trig = 29
u3Echo = 31

# Function to get the reading from a sensor
# Function is a modified version of 
# http://www.bytecreation.com/blog/2013/10/13/raspberry-pi-ultrasonic-sensor-hc-sr04

def reading(trigger, echo):
	
	# Disable any warning message such as GPIO pins in use
	#print("Set warnings to false")
	GPIO.setwarnings(False)
	
	# use the values of the GPIO pins, and not the actual pin number
	# so if you connect to GPIO 25 which is on pin number 22, the 
	# reference in this code is 25, which is the number of the GPIO 
	# port and not the number of the physical pin
	#print("Set mode")
  # I changed it. I like board better.
	GPIO.setmode(GPIO.BOARD)
	
	# point the software to the GPIO pins the sensor is using
	# change these values to the pins you are using
	# GPIO output = the pin that's connected to "Trig" on the sensor
	# GPIO input = the pin that's connected to "Echo" on the sensor
	#print("Setup pins")
	GPIO.setup(trigger, GPIO.OUT)
	GPIO.setup(echo ,GPIO.IN)
	GPIO.output(trigger, GPIO.LOW)
		
	# found that the sensor can crash if there isn't a delay here
	# no idea why. If you have odd crashing issues, increase delay
	#print("Sleeeeep")
	time.sleep(0.3)
		
	# sensor manual says a pulse ength of 10Us will trigger the 
	# sensor to transmit 8 cycles of ultrasonic burst at 40kHz and 
	# wait for the reflected ultrasonic burst to be received
		
	# to get a pulse length of 10Us we need to start the pulse, then
	# wait for 10 microseconds, then stop the pulse. This will 
	# result in the pulse length being 10Us.
		
	# start the pulse on the GPIO pin 
	# change this value to the pin you are using
	# GPIO output = the pin that's connected to "Trig" on the sensor
	#print("Trigger!")
	GPIO.output(trigger, True)
		
	# wait 10 micro seconds (this is 0.00001 seconds) so the pulse
	# length is 10Us as the sensor expects
	time.sleep(0.00001)
		
	# stop the pulse after the time above has passed
	# change this value to the pin you are using
	# GPIO output = the pin that's connected to "Trig" on the sensor
	#print("End trigger")
	GPIO.output(trigger, False)

	# listen to the input pin. 0 means nothing is happening. Once a
	# signal is received the value will be 1 so the while loop
	# stops and has the last recorded time the signal was 0
	# change this value to the pin you are using
	# GPIO input = the pin that's connected to "Echo" on the sensor
	#print("Wait...")
	signaloff = 0
	while GPIO.input(echo) == 0:
		signaloff = time.time()
		
	# listen to the input pin. Once a signal is received, record the
	# time the signal came through
	# change this value to the pin you are using
	# GPIO input = the pin that's connected to "Echo" on the sensor
	signalon = 0
	while GPIO.input(echo) == 1:
		signalon = time.time()
	#print("Found signal")
		
	# work out the difference in the two recorded times above to 
	# calculate the distance of an object in front of the sensor
	timepassed = signalon - signaloff
		
	# we now have our distance but it's not in a useful unit of
	# measurement. So now we convert this distance into centimetres
	distance = timepassed * 17000
		
	# return the distance of an object in front of the sensor in cm
	return distance
		
	# we're no longer using the GPIO, so tell software we're done
	# Disabled as we want to keep using them
  #GPIO.cleanup()


		
# Main program

while True:
	# Grab a reading
	reading1 = reading(u1Trig, u1Echo)
	reading2 = reading(u2Trig, u2Echo)
	reading3 = reading(u3Trig, u3Echo)

  # Average and print it out
	readingAvg = (reading1 + reading2 + reading3) / 3
	print(readingAvg)
