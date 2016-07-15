import RPi.GPIO as GPIO
import time

SERVO_PIN = 7
DISTANCE_IN_PIN = 11
DISTANCE_OUT_PIN = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(DISTANCE_OUT_PIN, GPIO.OUT)
GPIO.setup(DISTANCE_IN_PIN, GPIO.IN)
p = GPIO.PWM(SERVO_PIN, 50)
p.start(2.5)

def turn(angle):
	dutyCycle = 2.5 + angle/18.0
	# print "timeout: " + str(dutyCycle)
	p.ChangeDutyCycle(dutyCycle)

def distance():
	GPIO.output(DISTANCE_OUT_PIN, True)
	time.sleep(0.000002)
	GPIO.output(DISTANCE_OUT_PIN, False)

	while not GPIO.input(DISTANCE_IN_PIN):
		pass
	start = time.time()

	while GPIO.input(DISTANCE_IN_PIN):
		pass
	return (time.time() - start) * 17150

try:
	while True:
		angle = 0
		while angle<=180:
			turn(angle)
			angle += 15
			distance = distance()
			print("angle = "+str(angle)+"; distance="+str(distance) + " cm")
			time.sleep(0.1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
