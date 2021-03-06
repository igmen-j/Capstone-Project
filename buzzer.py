#=========================================================#
# buzzer.py                                               #
# File for the buzzer component                           #
#=========================================================#

import RPi.GPIO as GPIO
from setup import *

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Buzzer pin setup
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Function: buzzerSound
# Description: Allows the buzzer to buzz when it receives 1
# Parameters: onOrOff - receive 1 or 0
# Return: None
def buzzerSound(onOrOff):
    if onOrOff == 1:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
    else:
        GPIO.output(BUZZER_PIN, GPIO.LOW)
