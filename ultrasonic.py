#=========================================================#
# ultrasonic.py                                           #
# File for the ultrasonic component                       #
#=========================================================#
import RPi.GPIO as GPIO
import time

from setup import *

GPIO.setmode(GPIO.BCM)

# GPIO setup
GPIO.setup(TRIGGER_PIN_LEFT, GPIO.OUT)
GPIO.setup(ECHO_PIN_LEFT, GPIO.IN)
GPIO.setup(TRIGGER_PIN_FRONT, GPIO.OUT)
GPIO.setup(ECHO_PIN_FRONT, GPIO.IN)
GPIO.setup(TRIGGER_PIN_RIGHT, GPIO.OUT)
GPIO.setup(ECHO_PIN_RIGHT, GPIO.IN)


# Function: getDistance
# Description: Determines the distance with the obstacle and the sensor
# Parameters: trigger, echo
# Return: distance
def getDistance(trigger, echo):
    GPIO.output(trigger, False)
    time.sleep(0.000002)
    GPIO.output(trigger, True)
    time.sleep(0.000010)
    GPIO.output(trigger, False)

    startTime = time.time()
    endTime = time.time()

    # Sends echo signal out
    # Will break if endless loop
    break_start = time.time()
    while GPIO.input(echo) == 0:
        startTime = time.time()
        break_end = time.time()
        if break_end - break_start > 0.005:
            break
    
    # Receives echo signal
    # Will break if endless loop
    break_start = time.time()
    while GPIO.input(echo) == 1:
        endTime = time.time()
        break_end = time.time()
        if break_end - break_start > 0.005:
            break

    duration = endTime - startTime

    distance = (duration * 34300) / 2  # speed of sound = 34300 cm/s

    return distance
