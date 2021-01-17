import RPi.GPIO as GPIO
import time

DISTANCE_TO_BUZZ = 10

#subsystems
from buzzer import buzzerSound
from ultrasonic import getDistance

if __name__ == '__main__':
    while True:
        distance = getDistance()
        print("Distance: %.1f cm\n" % distance)
        if distance <= DISTANCE_TO_BUZZ:
            buzzerSound(1)
        else:
            buzzerSound(0)

