import RPi.GPIO as GPIO
import time

pin = 7
GPIO.output(3, False)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def turn(angle):
	timeout = (1 + angle/float(180))/float(1000)
	GPIO.output(pin, True)
	time.sleep(timeout)
	GPIO.output(pin, False)

while True:
	angle = 0
	while angle<=180:
		turn(angle)
		time.sleep(1)
		angle += 15
