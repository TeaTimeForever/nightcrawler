import RPi.GPIO as GPIO

from src.crawl.brain import find_wall_in_front

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

try:
	find_wall_in_front()
except KeyboardInterrupt:
	GPIO.cleanup()
