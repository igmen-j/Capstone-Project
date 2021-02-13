import RPi.GPIO as GPIO
#from pinList import *
from time import sleep

# Select GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(REMOTE_PIN, LED_PIN)

def readRemote(signal):
    if signal == 1:
        GPIO.output(REMOTE_PIN, GPIO.HIGH)
    else:
        GPIO.output(REMOTE_PIN, GPIO.LOW)
