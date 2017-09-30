from typing import Callable, List

import RPi.GPIO as GPIO
import time

from crawl.__types import Pin, Cm, Angle, CmPerSec
from crawl.rule import Rule

RIGHT: Angle = 0
FRONT: Angle = 90
LEFT: Angle = 180

_SONAR_FREQUENCY = 0.1
_SERVO_TIMEOUT = 0.3


class Sonar:

	def __init__(self, trigger_pin: Pin, echo_pin: Pin):
		self._trigger_pin = trigger_pin
		self._echo_pin = echo_pin
		GPIO.setup(self._trigger_pin, GPIO.OUT)
		GPIO.setup(self._echo_pin, GPIO.IN)

	def wait_until(self, predicate: Callable[[Cm], bool]):
		while predicate(self.distance()):
			time.sleep(_SONAR_FREQUENCY)

	def speed(self) -> CmPerSec:
		start = time.time()
		distances: List[Cm] = [self.distance() for _ in range(50)]
		duration = time.time() - start
		return 50 * sum([distance * (1225 - 50 * i) for i, distance in enumerate(distances)]) / 520625 / duration

	def distance(self) -> Cm:
		GPIO.output(self._trigger_pin, True)
		time.sleep(1 / 200000)
		GPIO.output(self._trigger_pin, False)
		while not GPIO.input(self._echo_pin):
			pass
		start = time.time()
		while GPIO.input(self._echo_pin):
			pass
		return (time.time() - start) * 17150


class RotatingSonar(Sonar):

	def __init__(self, trigger_pin: Pin, echo_pin: Pin, servo_pin: Pin):
		super().__init__(trigger_pin, echo_pin)
		GPIO.setup(servo_pin, GPIO.OUT)
		self._servo = GPIO.PWM(servo_pin, 50)
		self._angle: Angle = -1
		self.home()

	def wait_until(self, rules: List[Rule]) -> str:
		while True:
			for rule in rules:
				self.turn(rule.angle)
				distance = self.distance()
				if rule.predicate(distance):
					print(rule.key + ":" + str(distance))
					return rule.key
				time.sleep(_SONAR_FREQUENCY)

	def home(self):
		self.turn(FRONT)

	def turn(self, angle: Angle):
		if self._angle == angle:
			return
		dut_cycle = 2.25 + angle / 18
		self._servo.start(dut_cycle)
		time.sleep(_SERVO_TIMEOUT)
		self._servo.stop()
		self._angle = angle


ROTATING_SONAR = RotatingSonar(31, 32, 33)
