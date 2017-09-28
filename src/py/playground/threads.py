import threading
import time


class Threads:
	def __init__(self):
		self.speed1 = 0.0
		self.speed2 = 0.0
		self._t1 = threading.Thread(target=self.motor1)
		self._t1.start()
		self._t2 = threading.Thread(target=self.motor2)
		self._t2.start()

	def motor1(self):
		while True:
			print("motor1 speed = " + str(self.speed1))
			time.sleep(1)

	def motor2(self):
		while True:
			print("motor2 speed = " + str(self.speed2))
			time.sleep(1)

t = Threads()
time.sleep(3)
t.speed1 = 10.0
time.sleep(3)
t.speed2 = 20.0
