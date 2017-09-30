from typing import Callable

from crawl.__types import Angle, Cm


class Rule:

	def __init__(self, key: str, angle: Angle, predicate: Callable[[Cm], bool]):
		self.key = key
		self.angle = angle
		self.predicate = predicate
