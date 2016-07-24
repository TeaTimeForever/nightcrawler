import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)

GPIO.output(35, False)
GPIO.output(36, False)
GPIO.output(37, False)
GPIO.output(38, False)

def motorA(run, clockwise):
    if not run:
        GPIO.output(35, False)
        GPIO.output(36, False)
        return
    if clockwise:
        GPIO.output(35, False)
        GPIO.output(36, True)
    else:
        GPIO.output(36, False)
        GPIO.output(35, True)


def motorB(run, clockwise):
    if not run:
        GPIO.output(37, False)
        GPIO.output(38, False)
        return
    if clockwise:
        GPIO.output(37, False)
        GPIO.output(38, True)
    else:
        GPIO.output(38, False)
        GPIO.output(37, True)


while True:
    motorA(True, True)
    time.sleep(1)
    motorB(True, True)
    time.sleep(1)
    motorA(True, False)
    time.sleep(1)
    motorB(True, False)
    time.sleep(1)
    motorA(False,True)
    time.sleep(1)
    motorB(False, True)
    time.sleep(1)
