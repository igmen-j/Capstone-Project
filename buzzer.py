import RPi.GPIO as GPIO

from setup import *
from time import sleep

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Set buzzer - pin 23 as output
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def buzzerSound(onOrOff):
    if onOrOff == 1:
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
    else:
        GPIO.output(BUZZER_PIN, GPIO.LOW)