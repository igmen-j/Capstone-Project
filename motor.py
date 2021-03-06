#=========================================================#
# motor.py                                                #
# File for the motor component                            #
#=========================================================#

# Import required modules
import time
import RPi.GPIO as GPIO

from setup import *

# Declare the GPIO settings
GPIO.setmode(GPIO.BCM)

# set up GPIO pins
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)

pwm = GPIO.PWM(PWM_PIN, PWM_FREQUENCY)
pwm.start(0)   # stop first

# Function: changeDutyCycle
# Description: Changes the duty cycle of the motors
# Parameters: dutyCycle
# Return: None
def changeDutyCycle(dutyCycle):
    pwm.ChangeDutyCycle(dutyCycle)

# Function: goLeft
# Description: Moves the motor to the left
# Parameters: None
# Return: None
def goLeft():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.IN)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(RIGHT_MOTOR_INA, GPIO.HIGH)
    
# Function: goRight
# Description: Moves the motor to the right
# Parameters: None
# Return: None
def goRight():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(LEFT_MOTOR_INA, GPIO.HIGH)

# Function: goForward
# Description: Moves the motor forward
# Parameters: None
# Return: None
def goForward():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.OUT)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)
    GPIO.output(LEFT_MOTOR_INA, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_INA, GPIO.HIGH)

# Function: stopMotors
# Description: Stops all the motors
# Parameters: None
# Return: None
def stopMotors():
    GPIO.setup(LEFT_MOTOR_INA, GPIO.IN)
    GPIO.setup(LEFT_MOTOR_INB, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INA, GPIO.IN)
    GPIO.setup(RIGHT_MOTOR_INB, GPIO.IN)

    
    
