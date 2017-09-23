from crawl.__types import Distance
import crawl.drive as drive
import crawl.sonar as sonar
from crawl.rule import Rule

_MIN_FRONT_DISTANCE: Distance = 20
_SIDE_DISTANCE: Distance = _MIN_FRONT_DISTANCE + 10
_DISTANCE_TOLERANCE: Distance = 5
ROTATING_SONAR = sonar.RotatingSonar(31, 32, 33)


_FRONT_RULE =\
	Rule("front", sonar.FRONT, lambda distance: distance < _MIN_FRONT_DISTANCE)
_LEFT_TOO_FAR_RULE =\
	Rule("left_too_far", sonar.LEFT, lambda distance: distance > _SIDE_DISTANCE + _DISTANCE_TOLERANCE)
_LEFT_NOT_TOO_FAR_RULE = \
	Rule("left_not_too_far", sonar.LEFT, lambda distance: distance < _SIDE_DISTANCE + _DISTANCE_TOLERANCE)
_LEFT_TOO_CLOSE_RULE =\
	Rule("left_too_close", sonar.LEFT, lambda distance: distance < _SIDE_DISTANCE - _DISTANCE_TOLERANCE)
_LEFT_NOT_TOO_CLOSE_RULE = \
	Rule("left_not_too_close", sonar.LEFT, lambda distance: distance > _SIDE_DISTANCE - _DISTANCE_TOLERANCE)


def stop_at_wall_in_front():
	drive.forward()
	ROTATING_SONAR.wait_until([_FRONT_RULE])
	drive.stop()


def turn_sharp_right_until_wall_is_on_left():
	drive.sharp_turn_right()
	ROTATING_SONAR.wait_until([_LEFT_TOO_CLOSE_RULE])
	drive.stop()


def follow_the_wall() -> str:
	print("follow_the_wall")
	drive.forward()
	rule_id = ROTATING_SONAR.wait_until([_FRONT_RULE, _LEFT_TOO_CLOSE_RULE, _LEFT_TOO_FAR_RULE])
	drive.stop()
	return rule_id


def turn_right_until_wall_is_on_left():
	drive.turn_right()
	ROTATING_SONAR.wait_until([_FRONT_RULE, _LEFT_NOT_TOO_CLOSE_RULE])
	drive.stop()


def turn_left_until_wall_is_on_left():
	drive.turn_left()
	ROTATING_SONAR.wait_until([_FRONT_RULE, _LEFT_NOT_TOO_FAR_RULE])
	drive.stop()


_RULE_TO_ACTION_MAP = {
	"front": turn_sharp_right_until_wall_is_on_left,
	"left_too_far": turn_left_until_wall_is_on_left,
	"left_too_close": turn_right_until_wall_is_on_left
}


def crawl1():
	print("start crawling")
	stop_at_wall_in_front()
	rule_key = "front"
	while True:
		_RULE_TO_ACTION_MAP[rule_key]()
		rule_key = follow_the_wall()
