import RPi.GPIO as GPIO
import time

_FREQUENCY_SEC = 0.1
_SAMPLE_SIZE = 3

_SONAR_TRIGGER_PIN = 31
_SONAR_ECHO_PIN = 32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(_SONAR_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(_SONAR_ECHO_PIN, GPIO.IN)


def distance():
	return sum(
		[raw_distance() for _ in range(_SAMPLE_SIZE)]
	) / _SAMPLE_SIZE


def raw_distance():
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
		cm = distance()
		print(str(cm) + " cm")
		time.sleep(_FREQUENCY_SEC)
except KeyboardInterrupt:
	GPIO.cleanup()
