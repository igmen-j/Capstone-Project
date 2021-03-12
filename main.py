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
        changeDutyCycle(DEFAULT_PWM)
        
        print("Distance: %f" % distance) 

        # Checks the distance of obstacle and robot
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)        
        
        # Robot moves only when user is within 1m and 2m from the robot and there is not obstacle within 20cm
        if (distance > MIN_DISTANCE and distance < MAX_DISTANCE) and (distanceLeft > DISTANCE_TO_BUZZ and distanceFront > DISTANCE_TO_BUZZ_FRONT and distanceRight > DISTANCE_TO_BUZZ):
            buzzerSound(BUZZER_OFF)
            
            distance_div_one = MAX_DISTANCE / 3
            distance_div_two = MAX_DISTANCE * 2 / 3
            
            if distance <= distance_div_one or distance >= distance_div_two:
                distance_pwm_multiplier = 1.25
            else:
                distance_pwm_multiplier = 1
            
            if position == FAR_LEFT or position == FAR_RIGHT:
                position_pwm_multiplier = 1.5
            elif position == MID_LEFT or position == MID_RIGHT:
                position_pwm_multiplier = 1.25
            else:
                position_pwm_multiplier = 1    
            
            changeDutyCycle(DEFAULT_PWM*distance_pwm_multiplier*position_pwm_multiplier)
            
            if position == FAR_LEFT:
                goLeft()
                print("Far Left\n")
            elif position == MID_LEFT:
                goLeft()
                print("Mid Left\n")
            elif position == MIDDLE:
                goForward()
                print("Middle\n")
            elif position == MID_RIGHT:
                goRight()
                print("Mid Right\n")
            elif position == FAR_RIGHT:
                goRight()
                print("Far Right\n")
            else:
                stopMotors()
        else:
            buzzerSound(BUZZER_ON)
            stopMotors()
            print("Out of Bounds\n")
 
        time.sleep(0.1) 
