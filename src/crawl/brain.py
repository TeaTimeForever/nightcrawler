from src.crawl.drive import forward, stop
from src.crawl.sonar import Sonar
from src.crawl.types import Distance

_min_front_distance: Distance = 25
_side_distance: Distance = 25


def find_wall_in_front(sonar: Sonar):
	if sonar.distance() > _min_front_distance:
		forward()
		sonar.wait_until(lambda distance: distance < _min_front_distance)
		stop()

