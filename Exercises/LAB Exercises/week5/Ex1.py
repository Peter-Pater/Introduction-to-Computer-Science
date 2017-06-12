class Car:
	def __init__(self,year_model,make,speed):
		self.__year_model = year_model
		self.__speed = speed
		self.__make = make

	def accelerate(self):
		self.__speed = self.__speed + 5

	def brake(self):
		self.__speed = self.__speed - 5

	def get_speed(self):
		return self.__speed
