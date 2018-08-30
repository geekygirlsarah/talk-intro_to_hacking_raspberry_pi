# Intro to Hacking with the Raspberry Pi
# Sarah Withee
# Project 3

# Imports
import RPi_I2C_driver
import RPi.GPIO as GPIO
from time import *
from random import randint

# Wiring pin assignments
button_pins = [29, 31, 33]
led_pins = [19, 21, 23]

# Functions
def ledOn(pinNumber, on):
    GPIO.output(pinNumber, on)

def threeLedsOn(pins, redOn, greenOn, blueOn):
    ledOn(pins[0], redOn)
    ledOn(pins[1], greenOn)
    ledOn(pins[2], blueOn)

def threeLedsAllOff(pins):
    threeLedsOn(pins, False, False, False)

def getButtonPress():
    button_pressed = -1
    while button_pressed == -1:
        for j in range(0, len(button_pins)):
            if GPIO.input(button_pins[j]) == False:
                button_pressed = j
                print("Pressed: " + str(button_pressed))
                ledOn(led_pins[button_pressed], True)
                sleep(0.2)
    while GPIO.input(button_pins[button_pressed]) == False:
        sleep(0.001)  # just wait a bit

    ledOn(led_pins[button_pressed], False)
    return button_pressed

# Enable LCD screen
mylcd = RPi_I2C_driver.lcd()
mylcd.backlight(False)

# Setup button_pins and switches
GPIO.setmode(GPIO.BOARD)
for i in range(0, len(button_pins)):
    GPIO.setup(button_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led_pins[i], GPIO.OUT)
    GPIO.output(led_pins[i], False)

#-----------------------------------------------------------
#  Start the game!!!!!!
#-----------------------------------------------------------

# Are you ready?
mylcd.backlight(True)
mylcd.lcd_display_string("  Sarah Says!", 1)
mylcd.lcd_display_string("Press to start!", 2)
threeLedsOn(led_pins, True, True, True)

# Press any button to begin
button_pressed = False
getButtonPress()
threeLedsAllOff(led_pins)
mylcd.lcd_clear()
mylcd.backlight(False)

# Generate pattern
number_of_blinks = 3

pattern = []
for i in range(0, number_of_blinks):
    pattern.append(randint(0, 2))

print(pattern)

# Flash
length_of_flash = 1  #seconds
for i in range(0, number_of_blinks):
    if pattern[i] == 0:
        threeLedsOn(led_pins, True, False, False)
    elif pattern[i] == 1:
        threeLedsOn(led_pins, False, True, False)
    elif pattern[i] == 2:
        threeLedsOn(led_pins, False, False, True)
    sleep(length_of_flash)
    threeLedsAllOff(led_pins)
    sleep(0.5)


# Enter the pattern via button presses
mylcd.lcd_clear()
mylcd.lcd_display_string("Repeat the ", 1)
mylcd.lcd_display_string("pattern now!", 2)

winner = True
for i in range(number_of_blinks):
    # find button that's pressed
    button_pressed = getButtonPress()
    threeLedsAllOff(led_pins)

    # check button value against original pattern
    if button_pressed != pattern[i]:
        #loss :(
        mylcd.lcd_clear()
        mylcd.lcd_display_string("***  WRONG  ***", 1)
        mylcd.lcd_display_string("       :(      ", 2)
        winner = False
        break
    # else keep going...

# check winner variable to see what to do now
if winner:
    mylcd.lcd_clear()
    mylcd.lcd_display_string("Good job!!!", 1)

sleep(3)

mylcd.lcd_clear()
mylcd.backlight(False)

GPIO.cleanup()
