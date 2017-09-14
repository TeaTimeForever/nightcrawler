import RPi.GPIO as GPIO

from crawl import drive

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

try:
	# find_wall_in_front()
	drive._left_forward()
except KeyboardInterrupt:
	GPIO.cleanup()
