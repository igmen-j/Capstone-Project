#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(33, GPIO.OUT) # Connected to PWMA
GPIO.setup(37, GPIO.OUT) # Connected to AIN2
GPIO.setup(6, GPIO.OUT) # Connected to AIN1
#GPIO.setup(13, GPIO.OUT) # Connected to STBY

# Drive the motor clockwise
GPIO.output(12, GPIO.HIGH) # Set AIN1
#GPIO.output(11, GPIO.LOW) # Set AIN2

# Set the motor speed
GPIO.output(33, GPIO.HIGH) # Set PWMA

# Disable STBY (standby)
#GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Drive the motor counterclockwise
#GPIO.output(12, GPIO.LOW) # Set AIN1
#GPIO.output(11, GPIO.HIGH) # Set AIN2

# Set the motor speed
#GPIO.output(7, GPIO.HIGH) # Set PWMA

# Disable STBY (standby)
#GPIO.output(13, GPIO.HIGH)

# Wait 5 seconds
time.sleep(5)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(33, GPIO.LOW) # Set AIN1
GPIO.output(27, GPIO.LOW) # Set AIN2
GPIO.output(6, GPIO.LOW) # Set PWMA
#GPIO.output(13, GPIO.LOW) # Set STBY