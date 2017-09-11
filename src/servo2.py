import RPi.GPIO as GPIO
import time

pin = 33
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 0.5)

def turn(angle):
	timeout = .001 + angle/float(180000)
	print("timeout: " + str(timeout))
	GPIO.output(pin, True)
	time.sleep(timeout)
	GPIO.output(pin, False)

p.start(1)
