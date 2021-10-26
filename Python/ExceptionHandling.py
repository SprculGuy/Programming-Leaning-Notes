try:
	number = int(input('Enter a Number: '))
	if number%2:
		print(f'{number} is odd')
	else:
		print(f'{number} is even')
except ValueError:
	print('Please Enter Valid numeric value!')
