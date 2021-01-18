# import string, random

# # print(random.randint(1,1000))

# # example = list(string.ascii_lowercase)

# # print(random.choice(example))

# #DICE
# # class Die():
# # 	"""DICE MODULE"""
# # 	def __init__(self, sides=6):
# # 		self.sides = sides

# # 	def roll_die(self):
# # 		return random.randint(1, self.sides)


# # def times_rolled(sides, times):
# # 	dice = Die(sides)
# # 	for x in range(times):
# # 		print(f'Times rolled = {x + 1} and output is {dice.roll_die()}')
# # 		if x == 9:
# # 			break

# # def play_game():
# # 	sides = int(input("how many sides?"))
# # 	times = int(input("how many times to roll the dice"))
# # 	while sides != 0 or times != 0 :
# # 		times_rolled(sides, times)
# # 		sides = int(input("how many sides?"))
# # 		times = int(input("how many times to roll the dice"))
# # play_game()
# # print("finished")

# #Lottery

# def genNumber():
# 	lotteryNumber = ""
# 	rnum = 0
# 	for x in range(2):
# 		rnum = str(random.randint(0,100))
# 		if len(rnum) == 1:
# 			rnum = "0"+rnum
# 		lotteryNumber = lotteryNumber + rnum
# 	return lotteryNumber

# #myNumber 
# myNumber = (genNumber())

# #lotterNumber
# lotteryNumber = (genNumber())

# #GUI
# print(f'Your number was {int(myNumber):,}')

# #lucky number is
# print(f'Lottery winner number is {int(lotteryNumber):,}')

# # count the times it took Computer to get lucky numbet
# count = 0
# while myNumber != genNumber():
# 	count += 1

# print(f'It took Computer {count} random times to get this number!')

