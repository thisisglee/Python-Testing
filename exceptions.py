import json
# #try-except blocks
# n1 = ''
# while n1 != 'q':
# 	n1 = input("Enter first number or q to quit: ")
# 	if n1 == 'q':
# 		print("OK TATA!!")
# 		break
# 	n2 = input("Enter second number: ")
# 	try:
# 		answer = int(n1)/int(n2)
# 	except ZeroDivisionError:
# 		print(f"zero cant be divied or it might be the case that {n1} or {n2} is not a number ")
# 	except ValueError:
# 		print(f"It might be the case that {n1} or {n2} is not a number ")
# 		# pass is when you fail silently
# 		# pass
# #else is when try is true and thus is more resistant
# 	else:
# 		print(answer)

#CATS AND DOGS
def filereader(filename,letter):
	try:
		with open(filename) as f:
			contents = f.readlines()
	except:
		print(f"filename {filename} not found! PENCHO!, dekh directory")
	else:
		times = 0
		for c in contents:
			print(f'{c.rstrip()} is my pet')
			times += (c.count(letter))
		print(f'{times} times letter {letter} appeared')

#JSON_ JASCRIPT OBJECT NOTATION
def savecats(petname, filename):
	try:
		with open(filename, 'a') as f:
			#f.write(f'{petname}\n')
			json.append(petname, f)
	except:
		print(f"filename {filename} not found! PENCHO!, dekh directory")
	else:
		print(f'{petname} added to the file {filename}')
	finally:
		with open(filename) as f:
			contents = json.load(f)
		#for c in contents:
		print(f'{contents.rstrip()} is my pet')

savecats("Preeto", "dogs.json")
#filereader("cats.txt", "e")