from crawl.sonar import ROTATING_SONAR
from crawl.utils import max_min
from crawl.wheel import Wheel
from crawl.__types import Percent, Cm, CmPerSec

_RIGHT = Wheel(36, 35)
_LEFT = Wheel(37, 38)

_MIN_FRONT_DISTANCE: Cm = 20
_DISTANCE_TOLERANCE: Cm = 5
_MAX_ACCELERATION: Percent = 20
_SPEED_COEFFICIENT = 3
_MAX_SPEED: CmPerSec = 100


def _optimal_speed(distance: Cm) -> CmPerSec:
	return max_min((distance - _MIN_FRONT_DISTANCE) / _SPEED_COEFFICIENT, -_MAX_SPEED, _MAX_SPEED)


def _acceleration(current_speed: CmPerSec, optimal_speed: CmPerSec) -> Percent:
	return max_min(optimal_speed - current_speed, -_MAX_ACCELERATION, _MAX_ACCELERATION)


def slow_down_before_wall():
	distance = ROTATING_SONAR.distance()
	while abs(distance - _MIN_FRONT_DISTANCE) > _DISTANCE_TOLERANCE:
		distance = ROTATING_SONAR.distance()
		optimal_speed = _optimal_speed(distance)
		current_speed = ROTATING_SONAR.speed()
		acceleration = _acceleration(current_speed, optimal_speed)
		print(distance, current_speed, optimal_speed, acceleration)
		_RIGHT.accelerate(acceleration)
		_LEFT.accelerate(acceleration)
	stop()


def straight(gear: Percent):
	_RIGHT.speed(gear)
	_LEFT.speed(gear)


def stop():
	_RIGHT.stop()
	_LEFT.stop()


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

