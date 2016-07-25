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

def motorASpin(clockwise):
    if clockwise:
        GPIO.output(35, False)
        GPIO.output(36, True)
    else:
        GPIO.output(36, False)
        GPIO.output(35, True)

def motorBSpin(clockwise):
    if clockwise:
        GPIO.output(37, False)
        GPIO.output(38, True)
    else:
        GPIO.output(38, False)
        GPIO.output(37, True)

try:
    while True:
        motorASpin(True)
        time.sleep(1)
        motorBSpin(True)
        time.sleep(1)
        motorASpin(False)
        time.sleep(1)
        motorBSpin(False)
        time.sleep(1)
        motorAStop()
        time.sleep(1)
        motorBStop()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
