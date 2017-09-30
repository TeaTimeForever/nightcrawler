import RPi.GPIO as GPIO
from crawl.__types import Pin, Percent

_PWM_FREQUENCY = 50


class Wheel:

	def __init__(self, forward_pin: Pin, backward_pin: Pin):
		GPIO.setup(forward_pin, GPIO.OUT)
		GPIO.setup(backward_pin, GPIO.OUT)
		self._forward = GPIO.PWM(forward_pin, _PWM_FREQUENCY)
		self._backward = GPIO.PWM(backward_pin, _PWM_FREQUENCY)
		self._percent: Percent = 0
		self._forward.start(0)
		self._backward.start(0)

	def stop(self):
		self._forward.ChangeDutyCycle(0)
		self._backward.ChangeDutyCycle(0)
		self._percent = 0

	def accelerate(self, percent: Percent):
		self.go(self._percent + percent)

	def go(self, percent: Percent):
		print("wheel go " + str(percent))
		percent = _validate(percent)
		if self._percent == percent:
			return

		if percent >= 0:
			if self._percent < 0:
				self._backward.ChangeDutyCycle(0)
			self._forward.ChangeDutyCycle(percent)
		else:
			if self._percent > 0:
				self._forward.ChangeDutyCycle(0)
			self._backward.ChangeDutyCycle(-percent)

		self._percent = percent

	def close(self):
		self._forward.stop()
		self._backward.stop(0)


def _validate(percent: Percent) -> Percent:
	return 100.0 if percent > 100 else -100.0 if percent < -100 else percent
