import RPi.GPIO as GPIO
import time
from crawl.__types import Pin, Gear

_PIN_DELAY = 0.01

class Wheel:

	def __init__(self, forward_pin: Pin, backward_pin: Pin):
		GPIO.setup(forward_pin, GPIO.OUT)
		GPIO.setup(backward_pin, GPIO.OUT)
		self._forward = GPIO.PWM(forward_pin, 50)
		self._backward = GPIO.PWM(backward_pin, 50)
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
		print("new gear = " + str(self._gear))
		return abs(self._gear) == 100

	def go(self, gear: Gear):
		if gear > 100:
			gear = 100
		elif gear < -100:
			gear = -100
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
