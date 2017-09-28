from enum import Enum
import RPi.GPIO as GPIO
from crawl.__types import Pin, Speed


class Direction(Enum):
	FORWARD = 1
	BACKWARD = 2


class Wheel:

	def __init__(self, forward_pin: Pin, backward_pin: Pin):
		GPIO.setup(forward_pin, GPIO.OUT)
		GPIO.setup(backward_pin, GPIO.OUT)
		self._forward = GPIO.PWM(forward_pin, 50)
		self._backward = GPIO.PWM(backward_pin, 50)
		self._direction: Direction = None
		self._speed: Speed = 0

	def stop(self):
		self._forward.stop()
		self._backward.stop()
		self._speed = 0
		self._direction = None

	def forward(self, speed: Speed):
		if self._speed == speed and self._direction == Direction.FORWARD:
			return
		if self._direction == Direction.FORWARD:
			self._forward.ChangeDutyCycle(speed)
		else:
			if self._direction == Direction.BACKWARD:
				self._backward.stop()
			self._forward.start(speed)

	def backward(self, speed: Speed):
		if self._speed == speed and self._direction == Direction.BACKWARD:
				return
		if self._direction == Direction.BACKWARD:
			self._backward.ChangeDutyCycle(speed)
		else:
			if self._direction == Direction.FORWARD:
				self._forward.stop()
			self._backward.start(speed)
