# Reading entire file
# with open('pi_digits.txt') as file_object:
contents = (file_object.read()).rstrip()

# #check birthday  is in 1 millioin digts of pie 14/11/1998 - 14111998
# bday = "981230"

# if bday in contents:
# 	print("bday is in 1 million pi digits")

# else:
# 	print("bday not in 1 million digits of pi")

# # print(contents)

# # #read file line by line
# # with open("pi_digits.txt") as file_object:
# # 	for content in file_object:
# # 		print(content.rstrip())

# #or the dedicated way
# with open("pi_digits.txt") as file_object:
# 	lines = file_object.readlines()

# for line in lines:
# 	print(line.rstrip())

#writing to a file
#w - write and replace, a - append, add into next line, r+ - read and write
filename = 'firstwrite.txt'

# with open(filename, 'a') as file_object:
# 	file_object.write("Mera 6TH shehed chand\n")

# with open(filename) as file_object:
# 	contents = (file_object.read()).rstrip()

# print(contents)

##GUEST BOOK
guest = ''
while guest != 'q':
	guest = input("Please enter your name: ")
	if guest == 'q':
		print("ok sir g bye G!")
		break
	try:
		with open(filename,'a') as file_object:
			file_object.write(f'{guest} is here now\n')
	except:
		print("Something went wrong re")
	else:
		with open(filename) as file_object:
			print(file_object.read().rstrip())