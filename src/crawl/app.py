import RPi.GPIO as GPIO

from src.crawl.sonar import RotatingSonar

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ROTATING_SONAR = RotatingSonar(31, 32, 33)

try:
	while True:
		distance = measure_distance()
		print(str(distance) + " cm")
		time.sleep(1)
except KeyboardInterrupt:
	ROTATING_SONAR.close()
	GPIO.cleanup()