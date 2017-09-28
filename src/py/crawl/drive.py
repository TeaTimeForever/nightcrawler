import time

from crawl.wheel import Wheel
from crawl.__types import Pin, Speed

_RIGHT_FORWARD_PIN: Pin = 36
_RIGHT_BACKWARD_PIN: Pin = 35
_LEFT_FORWARD_PIN: Pin = 37
_LEFT_BACKWARD_PIN: Pin = 38

_RIGHT = Wheel(36, 35)
_LEFT = Wheel(37, 38)

_INERTIA_TIMEOUT: int = 0.3
_DC_FREQUENCY: int = 10


def forward(speed: Speed):
	print("forward")
	_RIGHT.forward(speed)
	_LEFT.forward(speed)


def backward(speed: Speed):
	print("backward")
	_RIGHT.backward(speed)
	_LEFT.backward(speed)


def stop():
	print("stop")
	_RIGHT.stop()
	_LEFT.stop()
	time.sleep(_INERTIA_TIMEOUT)


def turn_right():
	print("turn_right")


def sharp_turn_right():
	print("sharp_turn_right")


def turn_left():
	print("turn_right")


def sharp_turn_left():
	print("sharp_turn_right")

