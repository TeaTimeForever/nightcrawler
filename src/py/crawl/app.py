import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.brain import crawl1, forward_backward
from crawl import drive

# try:
# 	crawl1()
# except KeyboardInterrupt:
# 	GPIO.cleanup()

try:
	forward_backward()
except KeyboardInterrupt:
	drive.close()
	GPIO.cleanup()
