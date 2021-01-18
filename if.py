# cars=['audi','bmw','ford','honda']

# # for car in cars:
# # 	if car.lowe() == 'bmw':
# # 		print(car.upper())
# # 	else:
# # 		print(car.title())

# # print('bmw' in cars)		

# #alien invasion 
# alien_color = 'green'

# #if statement for score
# if alien_color == 'green':
# 	print('+5 points!')
# if alien_color == 'yellow':
# 	print('+10 points!')
# if alien_color == 'red':
# 	print('+15 points!')		

# #chcek onje list woth other
# my_cars=['audi','bmw','mercedes','honda']

# for my_car in my_cars:
# 	if my_car in cars:
# 		print(f"yes you can buy {my_car} from here.")
# 	else:
# 		print(f"{my_car} is not available.")
# print("fininshed printing")

# #Hello admin
# usernames=['admin','developer','accountant','HR','receptionist','cleaner']
# if usernames:
# 	for username in usernames:
# 		if username == 'admin':
# 			print("Hello admin, would you like to see a status report?")
# 		else:
# 			print(f'Hello {username}, thank you for logging in again')	
# else:
# 	print("LIST IS EMPTY")

# #Checking user name 
# employees = usernames[:]
# #print(employees)
# employees[4] = 'Desi adda'
# #print(employees)

# for employee in employees:
# 	if employee in usernames:
# 		print(f'{employee} works here')
# 	else:
# 		print(f'{employee} doesn\'t work here')

#ORDINAL NUMBERS

numbers = list(range(1,10))
#print(numbers)
for number in numbers:
	if number < 2:
		print("1st")
	elif number < 3:
		print("2nd")
	elif number < 4:
		print("3rd")
	else:
		print(f'{number}th')

