import RPi.GPIO as GPIO
import time

SERVO = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO, GPIO.OUT)
p = GPIO.PWM(SERVO, 50)
p.start(2.5)

def turn(angle):
	dutyCycle = 2.5 + angle/18.0
	# print "timeout: " + str(dutyCycle)
	p.ChangeDutyCycle(dutyCycle)

try:
	while True:
		angle = 0
		while angle<=180:
			turn(angle)
			print angle
			angle += 15
			time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
