def xxx():
	for x in range(10):
		for y in range(10):
			if x * y > 50:
				return
			else:
				print(str(x) + "-" + str(y))

xxx()
