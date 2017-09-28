from enum import Enum
import RPi.GPIO as GPIO
from crawl.__types import Pin, Speed


class Wheel:

	def __init__(self, forward_pin: Pin, backward_pin: Pin):
		GPIO.setup(forward_pin, GPIO.OUT)
		GPIO.setup(backward_pin, GPIO.OUT)
		self._forward = GPIO.PWM(forward_pin, 50)
		self._backward = GPIO.PWM(backward_pin, 50)
		self._speed: Speed = 0
		self._forward.start(0)
		self._backward.start(0)

	def stop(self):
		self._forward.ChangeDutyCycle(0)
		self._backward.ChangeDutyCycle(0)
		self._speed = 0

	def go(self, speed: Speed):
		if self._speed == speed:
			return

		if speed == 0:
			self.stop()
			return

		if speed > 0:
			if self._speed < 0:
				self._backward.ChangeDutyCycle(0)
			self._forward.ChangeDutyCycle(speed)
		else:
			if self._speed > 0:
				self._forward.ChangeDutyCycle(0)
			self._backward.ChangeDutyCycle(speed)

		self._speed = speed

	def close(self):
		self._forward.stop()
		self._backward.stop(0)
