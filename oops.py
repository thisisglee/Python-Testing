# #to make a model of Dog
# class Dog():
# 	""" Model of DOG"""
# 	def __init__(self, name, age):
# 		""" Constructor"""
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		""" command to make dog sit"""
# 		print(f'{self.name} ! Please sit')

# 	def roll_over(self):
# 		"""command to make dog roll over"""
# 		print(f'{self.name} ! you are now {self.age} years of age. please show us a roll over')

# zango = Dog('Zango', 4)

# Dog.sit(zango)

# Dog.roll_over(zango)	

class Car:
	"""A simple attempt to represent a car."""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title() 

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage 

		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	"""docstring for ElectricCar"""
	def __init__(self, make, model, year):
		super(Car).__init__(make, model, year)
		
		