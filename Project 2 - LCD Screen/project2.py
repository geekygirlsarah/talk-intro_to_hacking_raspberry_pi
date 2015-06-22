# Sarah Withee
# Intro to Hacking with the Raspberry Pi
# 3/20/2015
# Project 2 - LCD Screen


# Requires RPi_I2C_driver.py for I2C and LCD screen
import RPi_I2C_driver
from time import *

# Create the object
mylcd = RPi_I2C_driver.lcd()

# Print happy welcome message on lines 1 and 3
mylcd.lcd_display_string("Welcome to", 1)
mylcd.lcd_display_string(" Nebraska.Code() !!", 3)
sleep(2) # 2 sec delay

# Erase screen
mylcd.lcd_clear()

# These are the char codes to start writing on each of the 4 rows
rows= [0x80, 0xC0, 0x94, 0xD4]

# Start our ball at these coordinates. (-1 for funny logic)
x = 0
y = -1
# Values to change X/Y by (either add 1 or add -1)
changex = 1
changey = 1

# Just keep bouncing, just keep bouncing...
while True:
	# Move the ball
  x = x + changex
	y = y + changey
	
	# We hit the top
  if x < 2:
		changex = 1
		x = 1
	# We hit the bottom
  if x >= 4:
		changex = -1
	# We hit the left
  if y < 1:
		y = 0
		changey = 1
	# We hit the right
  if y >= 19:
		changey = -1

	# Print debug statements
	#print ("")
	#print ("x:")
	#print (x)
	#print ("y:")
	#print (y)

  # Erase ball
	mylcd.lcd_clear()

  # Print ball's new location
	mylcd.lcd_display_string_pos("o",x,y)

  # Wait just a bit so we can actually see it
	sleep(.5)


