import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.IN)

while True:
	GPIO.output(3, True)
	time.sleep(1/200000)
	GPIO.output(3, False)

	while not GPIO.input(5):
		pass
	start = time.time()

	while GPIO.input(5):
		pass
	delta = time.time() - start
	distance = delta * 17150

	print(str(distance) + " cm")
	time.sleep(1)
