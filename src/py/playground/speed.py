from typing import List


def speed10(distances: List[float]):
	return sum([distance * (45 - 10 * i) for i, distance in enumerate(distances)]) / 825


def speed20(distances: List[float]):
	return sum([distance * (190 - 20 * i) for i, distance in enumerate(distances)]) / 13300


def speed50(distances: List[float]):
	return sum([distance * (1225 - 50 * i) for i, distance in enumerate(distances)]) / 520625

print(speed10([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(speed20([19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
