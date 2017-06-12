class Info:

	def __init__(self,name,address,age,phone_number):
		self.__name = name
		self.__address = address
		self.__age = age
		self.__phone_number = phone_number

	def set_name(self,name):
		self.__name = name
		return self.__name

	def set_address(self,address):
		self.__address = address
		return self.__address

	def set_age(self,age):
		self.__age = age
		return self.__age

	def set_phone(self,phone_number):
		self.__phone_number = phone_number
		return self.__phone_number

	def get_name(self):
		return self.__name

	def get_address(self):
		return self.__address

	def get_age(self):
		return self.__age

	def get_phone(self):
		return self.__phone_number


