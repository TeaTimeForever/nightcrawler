from typing import Callable


def xxx(f: Callable[[int], bool]):
	print("its true") if f(7) else print("its false")


xxx(lambda x: x + 5)
