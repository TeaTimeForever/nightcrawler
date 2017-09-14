import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.brain import find_wall_in_front

try:
	find_wall_in_front()
except KeyboardInterrupt:
	GPIO.cleanup()
