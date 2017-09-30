import RPi.GPIO as GPIO
import time
from crawl.__types import Pin, Gear

_PIN_DELAY = 0.01
_MAX_GEAR = 100
_PWM_FREQUENCY = 10

class Wheel:

	def __init__(self, forward_pin: Pin, backward_pin: Pin):
		GPIO.setup(forward_pin, GPIO.OUT)
		GPIO.setup(backward_pin, GPIO.OUT)
		self._forward = GPIO.PWM(forward_pin, _PWM_FREQUENCY)
		self._backward = GPIO.PWM(backward_pin, _PWM_FREQUENCY)
		self._gear: Gear = 0
		self._forward.start(0)
		self._backward.start(0)

	def stop(self):
		self._forward.ChangeDutyCycle(0)
		self._backward.ChangeDutyCycle(0)
		time.sleep(_PIN_DELAY)
		self._gear = 0

	def accelerate(self, gear: Gear) -> bool:
		self.go(self._gear + gear)
		return abs(self._gear) == _MAX_GEAR

	def go(self, gear: Gear):
		if gear > _MAX_GEAR:
			gear = _MAX_GEAR
		elif gear < -_MAX_GEAR:
			gear = -_MAX_GEAR
		if self._gear == gear:
			return

		if gear >= 0:
			if self._gear < 0:
				self._backward.ChangeDutyCycle(0)
				time.sleep(_PIN_DELAY)
			self._forward.ChangeDutyCycle(gear)
		else:
			if self._gear > 0:
				self._forward.ChangeDutyCycle(0)
				time.sleep(_PIN_DELAY)
			self._backward.ChangeDutyCycle(-gear)

		self._gear = gear

	def close(self):
		self._forward.stop()
		self._backward.stop(0)
