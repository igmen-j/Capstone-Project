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
GPIO.setup(16, GPIO.OUT)


DISTANCE_TO_BUZZ = 10

if __name__ == '__main__':
    while True:
 
        getCamera()        

        distance, position = getCamera()
        changeDutyCycle(20)
        
        print("Distance: %f" % distance)      
        if distance > 1 and distance < 2:
            print("%s\n" % position)
            if position == "LEFT":
                goLeft()
            elif position == "RIGHT":
                goRight()
            elif position == "MIDDLE":
                goForward()
            else:
                stopMotors()
        else:
            stopMotors()
            print("Out of Bounds\n")
        
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)
                    
       # print("Left: %.1f cm  |  Front: %.1f cm  |  Right: %.1f cm\n" % (distanceLeft, distanceFront, distanceRight))
        if distanceLeft <= DISTANCE_TO_BUZZ or distanceFront <= DISTANCE_TO_BUZZ or distanceRight <= DISTANCE_TO_BUZZ:
            buzzerSound(1)
            stopMotors()
        else:
            buzzerSound(0)

        time.sleep(0.1)

