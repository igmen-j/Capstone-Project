#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
# set up GPIO pins
GPIO.setup(12, GPIO.OUT)  # Connected to PWMA
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#pwm = GPIO.PWM(12, 100)
#DC = 0
#pwm.start(50)
#GPIO.setup(37, GPIO.OUT)  # Connected to AIN2

while True:
    # pwm.ChangeDutyCycle(30)
    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    # time.sleep(3)
    #pwm.ChangeDutyCycle(30)

