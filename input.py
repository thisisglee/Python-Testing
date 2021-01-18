# # input function
# message = input("tell me something and I will repeat to you: \n")
# print(message.title())
# print(message.upper())
# print(message.lower())

# number = input('enter an number to have a cube of it: ')
# print(int(number)**3)


# def to_camel_case(text):
#     if text != "":
#         temp = text[:]    
#         temp = temp.replace('_', " ")
#         temp = temp.replace('-', " ")
#         temp = temp.title()
#         temp = temp.replace(' ', "")
#         new = f'{text[0]}{temp[1:]}'
#         print(new)
#         return new
#     else:
#     	return text

# to_camel_case('the_stealth_warrior')

def disemvowel(string):
    vowels = ['a','e','i','o','u']
    temp = ''
    for i in range(len(string)):
    	if string[i].lower() not in vowels:
    		temp += string[i]
    return temp

disemvowel('This website is for losers LOL!')

def iq_test(numbers):
    numbers = numbers.replace(' ', "")
    even_time = 0
    for i in range(0,3):
        if int(numbers[i]) % 2 == 0:
            even_time += 1
    #if even
    if even_time > 1:
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 != 0:
                return i + 1
    else:
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 == 0:
                return i + 1

iq_test()