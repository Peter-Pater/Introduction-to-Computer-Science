class Car:
	def __init__(self, speed, name):
		self.speed = speed
		self.name = name

	def get_speed(self):
		return self.speed

	def __str__(self):
		return "Car name is: %s" % (self.name)

car1 = Car(15, 'BMW')

print(car1.get_speed())
print(car1.name)


