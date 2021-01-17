import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIGGER_PIN = 18    #physical pin 12
ECHO_PIN = 24       #physical pin 18

GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def getDistance():
    GPIO.output(TRIGGER_PIN, False)
    time.sleep(0.000002)
    GPIO.output(TRIGGER_PIN, True)
    time.sleep(0.000010)
    GPIO.output(TRIGGER_PIN, False)

    while GPIO.input(ECHO_PIN) == 0:
        startTime = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        endTime = time.time()

    duration = endTime - startTime

    distance = (duration * 34300) / 2   # speed of sound = 34300 cm/s

    return distance

if __name__ == '__main__':
    while True:
        distance = getDistance()
        print("Distance: %.1f cm\n" % distance)









