import RPi.GPIO as GPIO
from time import sleep

# Select GPIO mode
GPIO.setmode(GPIO.BCM)

# Set buzzer - pin 23 as output
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)

def buzzerSound(onOrOff):
    if onOrOff == 1:
        GPIO.output(buzzer, GPIO.HIGH)
    else:
        GPIO.output(buzzer, GPIO.LOW)