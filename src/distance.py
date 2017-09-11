import RPi.GPIO as GPIO
import time

_SONAR_TRIGGER_PIN = 31
_SONAR_ECHO_PIN = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(_SONAR_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(_SONAR_ECHO_PIN, GPIO.IN)


def measure_distance() -> float:
	GPIO.output(_SONAR_TRIGGER_PIN, True)
	time.sleep(1/200000)
	GPIO.output(_SONAR_TRIGGER_PIN, False)

	while not GPIO.input(_SONAR_ECHO_PIN):
		pass
	start = time.time()

	while GPIO.input(_SONAR_ECHO_PIN):
		pass
	delta = time.time() - start
	return delta * 17150


try:
	while True:
		distance = measure_distance()
		print(str(distance) + " cm")
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
