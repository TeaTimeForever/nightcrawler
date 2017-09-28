import RPi.GPIO as GPIO

from crawl import drive

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.brain import crawl1, forward_backward

# try:
# 	crawl1()
# except KeyboardInterrupt:
# 	GPIO.cleanup()

try:
	forward_backward()
except KeyboardInterrupt:
	drive.close()
	GPIO.cleanup()
