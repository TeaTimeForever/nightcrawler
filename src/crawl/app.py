import RPi.GPIO as GPIO

from src.crawl import drive
from src.crawl.brain import find_wall_in_front

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

try:
	# find_wall_in_front()
	drive._left_forward()
except KeyboardInterrupt:
	GPIO.cleanup()
