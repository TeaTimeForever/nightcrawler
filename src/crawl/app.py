import RPi.GPIO as GPIO

from src.crawl.brain import find_wall_in_front
from src.crawl.sonar import RotatingSonar

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ROTATING_SONAR = RotatingSonar(31, 32, 33)

try:
	find_wall_in_front()
except KeyboardInterrupt:
	ROTATING_SONAR.close()
	GPIO.cleanup()