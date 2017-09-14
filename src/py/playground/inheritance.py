class A:
	_var1: int

	def __init__(self, var1: int):
		self._var1 = var1


class B(A):
	_var2: int

	def __init__(self, var1: int, var2: int):
		super().__init__(var1)
		self._var2 = var2

	def xxx(self):
		print(self._var1 + self._var2)


B(1, 2).xxx()
