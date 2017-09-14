import RPi.GPIO as GPIO

from crawl.types import Pin

_RIGHT_FORWARD_PIN: Pin = 35
_RIGHT_BACKWARD_PIN: Pin = 36
_LEFT_FORWARD_PIN: Pin = 37
_LEFT_BACKWARD_PIN: Pin = 38
GPIO.setup(_RIGHT_FORWARD_PIN, GPIO.OUT)
GPIO.setup(_RIGHT_BACKWARD_PIN, GPIO.OUT)
GPIO.setup(_LEFT_FORWARD_PIN, GPIO.OUT)
GPIO.setup(_LEFT_BACKWARD_PIN, GPIO.OUT)

GPIO.output(_RIGHT_FORWARD_PIN, False)
GPIO.output(_RIGHT_BACKWARD_PIN, False)
GPIO.output(_LEFT_FORWARD_PIN, False)
GPIO.output(_LEFT_BACKWARD_PIN, False)


def _right_stop():
	GPIO.output(_RIGHT_FORWARD_PIN, False)
	GPIO.output(_RIGHT_BACKWARD_PIN, False)


def _left_stop():
	GPIO.output(_LEFT_FORWARD_PIN, False)
	GPIO.output(_LEFT_BACKWARD_PIN, False)


def _right_forward():
	GPIO.output(_RIGHT_BACKWARD_PIN, False)
	GPIO.output(_RIGHT_FORWARD_PIN, True)


def _right_backward():
	GPIO.output(_RIGHT_FORWARD_PIN, False)
	GPIO.output(_RIGHT_BACKWARD_PIN, True)


def _left_forward():
	GPIO.output(_LEFT_BACKWARD_PIN, False)
	GPIO.output(_LEFT_FORWARD_PIN, True)


def _left_backward():
	GPIO.output(_LEFT_FORWARD_PIN, False)
	GPIO.output(_LEFT_BACKWARD_PIN, True)


def forward():
	_right_forward()
	_left_forward()


def backward():
	_right_backward()
	_left_backward()


def stop():
	_right_stop()
	_left_stop()


def turn_right():
	_right_stop()
	_left_forward()


def sharp_turn_right():
	_right_backward()
	_left_forward()


def turn_left():
	_left_stop()
	_right_forward()


def sharp_turn_left():
	_left_backward()
	_right_forward()
