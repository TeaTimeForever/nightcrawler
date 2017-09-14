from src.crawl.drive import forward, stop
from src.crawl.sonar import RotatingSonar
from src.crawl.types import Distance

_MIN_FRONT_DISTANCE: Distance = 25
_MIN_SIDE_DISTANCE: Distance = 25
ROTATING_SONAR = RotatingSonar(31, 32, 33)


def find_wall_in_front():
	if ROTATING_SONAR.distance() > _MIN_FRONT_DISTANCE:
		forward()
		ROTATING_SONAR.wait_until(dict([(90, lambda distance: distance < _MIN_FRONT_DISTANCE)]))
		stop()
