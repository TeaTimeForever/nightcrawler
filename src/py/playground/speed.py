from typing import List


def speed(distances: List[float]):
	return sum([distance * (45 - 10 * i) for i, distance in enumerate(distances)]) / 825


print(speed([12, 11, 9, 12, 14, 13, 17, 16, 16, 17]))
