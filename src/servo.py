import RPi.GPIO as GPIO
import time

pin = 7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def turn(angle):
	timeout = .001 + angle/float(180000)
	print "timeout: " + str(timeout)
	GPIO.output(pin, True)
	time.sleep(timeout)
	GPIO.output(pin, False)

while True:
	angle = 0
	while angle<=180:
		turn(angle)
#		print angle
		time.sleep(1)
		angle += 15