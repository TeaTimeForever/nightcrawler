from typing import Callable, Dict, List

import RPi.GPIO as GPIO
import time

from crawl.__types import Pin, Distance, Angle
from crawl.rule import Rule

RIGHT: Angle = 0
FRONT: Angle = 90
LEFT: Angle = 180

_FREQUENCY = 0.1
_SAMPLE_SIZE = 3

_SERVO_FREQUENCY = 0.2


class Sonar:
	_trigger_pin: int
	_echo_pin: int

	def __init__(self, trigger_pin: Pin, echo_pin: Pin):
		self._trigger_pin = trigger_pin
		self._echo_pin = echo_pin
		GPIO.setup(self._trigger_pin, GPIO.OUT)
		GPIO.setup(self._echo_pin, GPIO.IN)

	def wait_until(self, predicate: Callable[[Distance], bool]):
		while predicate(self.distance()):
			time.sleep(_FREQUENCY)

	def distance(self) -> Distance:
		return sum([self._raw_distance() for _ in range(_SAMPLE_SIZE)]) / _SAMPLE_SIZE

	def _raw_distance(self) -> Distance:
		GPIO.output(self._trigger_pin, True)
		time.sleep(1 / 200000)
		GPIO.output(self._trigger_pin, False)
		while not GPIO.input(self._echo_pin):
			pass
		start = time.time()
		while GPIO.input(self._echo_pin):
			pass
		delta = time.time() - start
		return delta * 17150


class RotatingSonar(Sonar):
	_servo_pwm: any

	def __init__(self, trigger_pin: Pin, echo_pin: Pin, servo_pin: Pin):
		super().__init__(trigger_pin, echo_pin)
		GPIO.setup(servo_pin, GPIO.OUT)
		self._servo_pwm = GPIO.PWM(servo_pin, 50)
		self._servo_pwm.start(2.5)
		self.home()

	def wait_until(self, rules: List[Rule]) -> str:
		while True:
			for rule in rules:
				self.turn(rule.angle)
				distance = self.distance()
				if rule.predicate(distance):
					print(rule.key + ":" + str(distance))
					return rule.key
				time.sleep(_SERVO_FREQUENCY)

	def home(self):
		self.turn(FRONT)

	def turn(self, angle: int):
		dut_cycle = 2.5 + angle / 18.0
		self._servo_pwm.ChangeDutyCycle(dut_cycle)
		time.sleep(0.01)

	def close(self):
		self._servo_pwm.stop()
