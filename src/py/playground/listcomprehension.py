import random


def xxx() -> float:
	return random.randint(1,11)


print(sum([xxx() for _ in range(3)]))

print([100] * 3)

print(([xxx] * 3)[0]())


def distance():
	return sum(
		[xxx() for _ in range(3)]
	) / 3
