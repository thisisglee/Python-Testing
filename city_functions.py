def city_country(city, country, population=''):
	if population != '':
		temp = f'{city}, {country} = {str(population)}'
	else:
		temp = f'{city}, {country}'
	return temp

print(city_country('santiago', 'chile', '5000000'))