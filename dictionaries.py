# # NEW_DICTIONARY = {'ATTRIBUTE':'VALUE'}
# #PRINT(NEW_DI)
# alien_0 = {}
# alien_0 = {'color':'green','points':'5'}

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0['position-x'] = 0
# alien_0['position-y'] = 25

# print(alien_0)

# alien_0['speed'] = 'medium'

# #Changing position of alien on x-axis depending on its speed
# print(f'position of alien_0 = ({alien_0["position-x"]}, {alien_0["position-y"]}) and speed is {alien_0["speed"]}')
# x_increment = 0
# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# elif alien_0['speed'] == 'fast':
# 	x_increment = 3

# #change in position
# alien_0['position-x'] = x_increment + alien_0['position-x'] 
# print(f'change in position is {x_increment} so new postion is {alien_0["position-x"]} ')

# #Deleting a Key
# del alien_0['points']

# print(alien_0)

# # del alien_0
# # print(alien_0)

# fav_foods = {
# 	'glee':'butter chicken',
# 	'gurleen':'mushroom duplex',
# }

# #get is useful when calling a key and returns a statement if key does not exist
# print(alien_0.get('points', 'no points found'))

# #person
# person = {
# 	'first_name': 'Gurleen',
# 	'last_name': 'Maggon',
# 	'city': 'Barrie',
# }

# for key, value in person.items():
# 	print(f'{key} is ')
# 	print(f'{value}. \n')

# for key in person.keys():
# 	print(key)

# favorite_languages = { 
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': 'python',
# 	}
# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
# 	print(f'Hi {name}!')

# 	#if name matches
# 	# if name in friends:
# 	# 	print(f'\t Ahh!! {name.title()} I see you like {favorite_languages[name]}')

# for name in sorted(favorite_languages.keys()):
# 	print(f'Hi {name}!')

# #NESTING - list of lsits or dictionaries
# alien_0 = {'color': 'green', 'points': 5} 
# alien_1 = {'color': 'yellow', 'points': 10} 
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2] 
# for alien in aliens: 
# 	print(alien)

# #dictionary of lists
# dictname = {'Phil':['C','Java','Python']}

# print(dictname)


#delete occurence of a n element if it occurs mor=e than one time
def delete_nth(order):
    dict1 = {}
    temp = []
    ocurence = 0
    for i in range(len(order)):
        if order[i] in list(dict1.keys()):
            ocurence = dict1.get(order[i])
        else:
            ocurence = 0
        if ocurence < len(order):
            ocurence += 1
            dict1[order[i]] = ocurence 
    print (dict1)
    # return temp
    sort_orders = sorted(dict1.items(), key=lambda x: x[1])
    for i in sort_orders:
        print(i[0], i[1])

delete_nth(order = [5,3,1,2,2,4])

#13422
