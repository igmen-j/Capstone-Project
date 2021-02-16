#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
# set up GPIO pins
GPIO.setup(12, GPIO.OUT)  # Connected to PWMA
#GPIO.setup(16, GPIO.OUT)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
#GPIO.setup(18, GPIO.IN)

pwm = GPIO.PWM(12, 1000)
pwm.start(50)
#GPIO.setup(37, GPIO.OUT)  # Connected to AIN2

while True:
    pwm.ChangeDutyCycle(10)
    
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(18, GPIO.IN)
    time.sleep(0.5)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.setup(16, GPIO.IN)
    time.sleep(0.5)
