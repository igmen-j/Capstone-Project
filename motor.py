#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

from pinList import *

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)

pwm = GPIO.PWM(PWM_PIN, PWM_FREQUENCY)
pwm.start(0)   # stop first

def changeDutyCycle(dutyCycle):
    pwm.ChangeDutyCycle(PWM_PIN, dutyCycle)

def goLeft():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.IN)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(RIGHT_MOTOR_INA, GPIO.HIGH)
    

def goRight():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(LEFT_MOTOR_INA, GPIO.HIGH)

def goForward():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(LEFT_MOTOR_INA, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_INA, GPIO.HIGH)

def stopMotors():
    GPIO.output(LEFT_MOTOR_INA, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_INA, GPIO.LOW)
    GPIO.output(LEFT_MOTOR_INB, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_INB, GPIO.LOW)
    GPIO.setup(LEFT_MOTOR_INA, GPIO.IN)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)