import RPi.GPIO as GPIO
import time

#subsystems
import buzzer
from ultrasonic import getDistance

if __name__ == '__main__':
    while True:
        distance = getDistance()
        print("Distance: %.1f cm\n" % distance)
