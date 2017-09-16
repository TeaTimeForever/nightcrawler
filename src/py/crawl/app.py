import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.brain import crawl1

try:
	crawl1()
except KeyboardInterrupt:
	GPIO.cleanup()
