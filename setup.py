#=========================================================#
# setup.py                                                #
# Determines the pin list and settings                    #
#=========================================================#


TRIGGER_PIN_LEFT  = 18    # physical pin 12
ECHO_PIN_LEFT     = 24    # physical pin 18
TRIGGER_PIN_FRONT = 17    # physical pin 11
ECHO_PIN_FRONT    = 27    # physical pin 13
TRIGGER_PIN_RIGHT = 5     # physical pin 29
ECHO_PIN_RIGHT    = 6     # physical pin 31

BUZZER_PIN        = 23    # physical pin 16
REMOTE_PIN        = 26    # physical pin 37

LEFT_MOTOR_INA    = 20    # physical pin 38
LEFT_MOTOR_INB    = 21    # physical pin 40
RIGHT_MOTOR_INA   = 7     # physical pin 26
RIGHT_MOTOR_INB   = 1     # physical pin 28
PWM_PIN           = 12    # physical pin 32

PWM_FREQUENCY     = 1000
DISTANCE_TO_BUZZ  = 10
DEFAULT_PWM       = 33

FAR_LEFT          = 0
MID_LEFT          = 1
MIDDLE            = 2
MID_RIGHT         = 3
FAR_RIGHT         = 4
OUT_OF_RANGE      = 1000
