import RPi.GPIO as GPIO
import time import sleep

#Select GPIO mode
GPIO.setmode(GPIO.BCM)

#Set buzzer - pin 23 as output
buzzer=23
GPIO.setup(buzzer,GPIO.OUT)
p = IO.pwm(buzzer,100)
p.start(0)
#Run forever loop

while 1:
    for x in range (50):
        p.ChangeDutyCycle(x)
        sleep(0.1)
    for x in range (50):
        p.ChangeDutyCycle(50-x)
        sleep(0.1)

#while True:
#    GPIO.output(buzzer,GPIO.HIGH)
#    sleep(0.5) # Delay in seconds
#    GPIO.output(buzzer,GPIO.LOW)
#    sleep(0.5)