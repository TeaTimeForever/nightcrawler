import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

from crawl.drive import forward, stop

from crawl.brain import crawl1

# try:
# 	crawl1()
# except KeyboardInterrupt:
# 	GPIO.cleanup()

try:
	forward(10)
	time.sleep(10)
except KeyboardInterrupt:
	stop()
	GPIO.cleanup()
