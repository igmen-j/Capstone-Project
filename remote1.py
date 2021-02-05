import RPi.GPIO as GPIO
#from pinList import *
from time import sleep

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Remote PIN: GPIO 16 or pin 36
# LED PIN: GPIO 6 or pin 31

REMOTE_PIN = 26
LED_PIN = 25

GPIO.setup(REMOTE_PIN, LED_PIN)

def readRemote(x):
    if x == 1:
        GPIO.output(REMOTE_PIN, GPIO.HIGH)
    else:
        GPIO.output(REMOTE_PIN, GPIO.LOW)