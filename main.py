import RPi.GPIO as GPIO
import time
from pinList import *

DISTANCE_TO_BUZZ = 10

#subsystems
from buzzer import buzzerSound
from ultrasonic import getDistance

if __name__ == '__main__':
    while True:
        distanceLeft = getDistance(TRIGGER_PIN_LEFT, ECHO_PIN_LEFT)
        distanceFront = getDistance(TRIGGER_PIN_FRONT, ECHO_PIN_FRONT)
        distanceRight = getDistance(TRIGGER_PIN_RIGHT, ECHO_PIN_RIGHT)
        print("Left: %.1f cm  |  Front: %.1f cm  |  Right: %.1f cm\n" % (distanceLeft, distanceFront, distanceRight))
        if distanceLeft <= DISTANCE_TO_BUZZ or distanceFront <= DISTANCE_TO_BUZZ or distanceRight <= DISTANCE_TO_BUZZ:
            buzzerSound(1)
        else:
            buzzerSound(0)

        time.sleep(1)

