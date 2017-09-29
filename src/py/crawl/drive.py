import time

from crawl.sonar import ROTATING_SONAR
from crawl.wheel import Wheel
from crawl.__types import Pin, Gear, Distance, Speed

_RIGHT_FORWARD_PIN: Pin = 36
_RIGHT_BACKWARD_PIN: Pin = 35
_LEFT_FORWARD_PIN: Pin = 37
_LEFT_BACKWARD_PIN: Pin = 38

_RIGHT = Wheel(36, 35)
_LEFT = Wheel(37, 38)

_INERTIA_TIMEOUT: int = 0.3
_DC_FREQUENCY: int = 10

_MIN_FRONT_DISTANCE: Distance = 20
_DISTANCE_TOLERANCE: Distance = 5


def slow_down_before_wall():
	while abs(ROTATING_SONAR.distance() - _MIN_FRONT_DISTANCE) > _DISTANCE_TOLERANCE:
		distance1 = ROTATING_SONAR.distance()
		time.sleep(_INERTIA_TIMEOUT)
		distance2 = ROTATING_SONAR.distance()
		speed = (distance2 - distance1) / _INERTIA_TIMEOUT
		delta_from_optimal_trajectory = distance2 - _MIN_FRONT_DISTANCE - speed * 2
		_RIGHT.accelerate(delta_from_optimal_trajectory)
		_LEFT.accelerate(delta_from_optimal_trajectory)
	stop()


def straight(gear: Gear):
	_RIGHT.go(gear)
	_LEFT.go(gear)


def stop():
	_RIGHT.stop()
	_LEFT.stop()
	time.sleep(_INERTIA_TIMEOUT)


def close():
	_RIGHT.close()
	_LEFT.close()


def turn_right():
	print("turn_right")


def sharp_turn_right():
	print("sharp_turn_right")


def turn_left():
	print("turn_right")


def sharp_turn_left():
	print("sharp_turn_right")

