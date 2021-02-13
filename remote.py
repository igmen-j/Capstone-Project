import RPi.GPIO as GPIO
#from pinList import *
from time import sleep

# Select GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(REMOTE_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def readRemote():
    if GPIO.input(REMOTE_PIN) == 1:
        GPIO.output(REMOTE_PIN, GPIO.HIGH)
    else:
        GPIO.output(REMOTE_PIN, GPIO.LOW)
