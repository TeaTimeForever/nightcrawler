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

def motorAStop():
    GPIO.output(35, False)
    GPIO.output(36, False)

def motorBStop():
    GPIO.output(37, False)
    GPIO.output(38, False)

def motorASpin(forward):
    if forward:
        GPIO.output(35, False)
        GPIO.output(36, True)
    else:
        GPIO.output(36, False)
        GPIO.output(35, True)

def motorBSpin(forward):
    if forward:
        GPIO.output(38, False)
        GPIO.output(37, True)
    else:
        GPIO.output(37, False)
        GPIO.output(38, True)


def forwardAndBackward():
    motorASpin(True)
    motorBSpin(True)
    time.sleep(3)
    motorAStop()
    motorBStop()
    time.sleep(0.5)
    motorASpin(False)
    motorBSpin(False)
    time.sleep(3)
    motorAStop()
    motorBStop()
    time.sleep(0.5)


def spin():
    motorASpin(True)
    motorBSpin(False)
    time.sleep(3)
    motorAStop()
    motorBStop()
    time.sleep(0.5)
    motorASpin(False)
    motorBSpin(True)
    time.sleep(3)
    motorAStop()
    motorBStop()
    time.sleep(0.5)


try:
    while True:
        '''forwardAndBackward()'''
        spin()

except KeyboardInterrupt:
    GPIO.cleanup()