#for value in range(1,100):
#	print(value)

#to make a list of numbers
numbers = list(range(1,11))
print(numbers)

# to make even numbers list
even_numbers = list(range(0,100,5))
print(even_numbers)

#to make a square of first 10 numbers
squares = []
for number in numbers:
	square = number**2
	squares.append(square)

print(squares)

#short form
new_squares = []
for value in range(1,101):
	new_squares.append(value**2)
print(new_squares)

eve = [value/2 for value in range(0,11)]
print(eve)

#counting to 20
for value in range(1,21):
	print(value)

#one million
million = []
million = [value for value in range(1,1_000_000)]

#sunmming a million
print(sum(million))

#odd numbers
numbers = list(range(1,21,2))
print(numbers)

# ifrst 10 cubes
cubes = [value**3 for value in range(0,11)]
print(cubes)

