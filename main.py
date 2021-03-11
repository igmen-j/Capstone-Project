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
from remote import readRemote

GPIO.setmode(GPIO.BCM)

if __name__ == '__main__':
    while True:     
        distance, position = getCamera()
        changeDutyCycle(DEFAULT_PWM)
        
        print("Distance: %f" % distance) 

        # Checks the distance of obstacle and robot
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)        
        
        # Robot moves only when user is within 1m and 2m from the robot and there is not obstacle within 20cm
        if (distance > MIN_DISTANCE and distance < MAX_DISTANCE) and (distanceLeft > DISTANCE_TO_BUZZ and distanceFront > DISTANCE_TO_BUZZ and distanceRight > DISTANCE_TO_BUZZ):
            buzzerSound(BUZZER_OFF)
            if position == FAR_LEFT:
                goLeft()
                changeDutyCycle(DEFAULT_PWM*1.5)
                print("Far Left\n")
            elif position == MID_LEFT:
                goLeft()
                changeDutyCycle(DEFAULT_PWM)
                print("Mid Left\n")
            elif position == MIDDLE:
                goForward()
                changeDutyCycle(DEFAULT_PWM)
                print("Middle\n")
            elif position == MID_RIGHT:
                goRight()
                changeDutyCycle(DEFAULT_PWM)
                print("Mid Right\n")
            elif position == FAR_RIGHT:
                goRight()
                changeDutyCycle(DEFAULT_PWM*1.5)
                print("Far Right\n")
            else:
                stopMotors()
        else:
            buzzerSound(BUZZER_OFF)
            stopMotors()
            print("Out of Bounds\n")
 
        time.sleep(0.1) 
