from __future__ import print_function

#import sys
#sys.path.append('../camera')

import RPi.GPIO as GPIO
import time

import os
from pinList import *

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
        ave_distance, position = getCamera()
        
        print("Distance: %f" % ave_distance)
        if ave_distance > 1 and ave_distance < 2:
            print("%s\n" % position)
        else:
            print("Out of Bounds\n")
        
        
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)
                    
       # print("Left: %.1f cm  |  Front: %.1f cm  |  Right: %.1f cm\n" % (distanceLeft, distanceFront, distanceRight))
        if distanceLeft <= DISTANCE_TO_BUZZ or distanceFront <= DISTANCE_TO_BUZZ or distanceRight <= DISTANCE_TO_BUZZ:
            buzzerSound(1)
        else:
            buzzerSound(0)

        time.sleep(0.1)

