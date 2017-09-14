import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl import drive

try:
	# find_wall_in_front()
	while True:
		drive._left_forward()
except KeyboardInterrupt:
	GPIO.cleanup()
