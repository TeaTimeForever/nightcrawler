from rx import Observable, Observer
import RPi.GPIO
import time
from enum import Enum

_FREQUENCY_SEC = 0.1
_SAMPLE_SIZE = 3

_SONAR_TRIGGER_PIN = 31
_SONAR_ECHO_PIN = 32
_SERVO_PIN = 33

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(_SONAR_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(_SONAR_ECHO_PIN, GPIO.IN)
GPIO.setup(_SERVO_PIN, GPIO.OUT)
p = GPIO.PWM(_SERVO_PIN, 50)
p.start(2.5)


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
		distance = measure_distance()
		print(str(distance) + " cm")
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()