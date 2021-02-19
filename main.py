#=================================================================#
# ENEL 417 Capstone Project                                       #
# Title: Bot Follower                                             #
# Group 9: Danny Hoang, Justin Igmen, Zain Khokhar                #
# Description: Robot the can lift things adn follow user around   #                                              
#=================================================================#

from __future__ import print_function

#import sys
#sys.path.append('../camera')

import RPi.GPIO as GPIO
import time

import os
from setup import *

#subsystems
import camera
from camera import *
from motor import *
from buzzer import buzzerSound
from ultrasonic import getDistance

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    while True:     
        distance, position = getCamera()
        changeDutyCycle(20)
        
        print("Distance: %f" % distance) 
	
	# Checks the distance of obstacle and robot
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)
		
	# Robot moves only when user is within 1m and 2m from the robot and there is not obstacle within 20cm
        if (distance > 1 and distance < 2) and (distanceLeft > DISTANCE_TO_BUZZ or distanceFront > DISTANCE_TO_BUZZ or distanceRight > DISTANCE_TO_BUZZ):
            print("%s\n" % position)
	    buzzerSound(0)
            if position == "LEFT":
                goLeft()
            elif position == "RIGHT":
                goRight()
            elif position == "MIDDLE":
                goForward()
            else:
                stopMotors()
        else:
	    buzzerSound(1)
            stopMotors()
            print("Out of Bounds\n")
 
                 

        time.sleep(0.1) 
