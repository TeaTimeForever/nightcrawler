def xxx() -> float:
	return 3.1428


print(sum([xxx() for _ in range(3)]))

print([100] * 3)


def distance():
	return sum(
		[xxx() for _ in range(3)]
	) / 3