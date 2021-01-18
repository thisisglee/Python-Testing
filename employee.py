class Employee():
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = int(pay)

	def give_raise(self, pay):
		self.pay = int(pay) + 5000
		return True
	
emp = Employee("kiddan","Veer",0)
