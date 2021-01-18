import unittest
#from name_function import get_formated_name
#from city_functions import city_country
from employee import Employee

# print(city_country('Delhi','India'))
# print(city_country('santiago', 'chile', '5000000'))

# assertEqual(a, b) Verify that a == b 
# assertNotEqual(a, b) Verify that a != b 
# assertTrue(x) Verify that x is True
# assertFalse(x) Verify that x is False 
# assertIn( item, list ) Verify that item is in list


# class NameTestCase(unittest.TestCase):
# 	"""Tests for name_function"""
# 	#Any method that starts with test_ will be run automatically
# 	def test_first_last_name(self):
# 		"""DO Names like 'Janis Joplin' work?"""
# 		formated_name = get_formated_name('Janis','Joplin')
# 		self.assertEqual(formated_name,'Janis Joplin')

# if __name__ == '__main__':
# 	unittest.main()

#city_functions is a module for test cases
# class CityTestCase(unittest.TestCase):
# 	"""tests for city_funcitons"""
# 	def test_city_country(self):
# 		# temp = city_country('santiago', 'chile')
# 		self.assertEqual(city_country('santiago', 'chile'), "santiago, chile")
		
# 	def test_city_country_population(self):
# 		self.assertEqual(city_country('santiago', 'chile', '5000000'), "santiago, chile = 5000000")

#employee is a module from employee class
class EmployeeTestCase(unittest.TestCase):
	"""tests for Employee class with setUp(method)"""
	def setUp(self):
		"""instances for the test cases"""
		self.emp = Employee("kiddan","Veer",0)

	def test_give_default_raise(self):
		self.assertTrue(self.emp.give_raise(0))

	def test_give_custom_raise(self):
		self.assertTrue(self.emp.give_raise(4000))


if __name__ == '__main__':
	unittest.main()