print('Welcome to Robot\'s game')
level = input('Enter level (1 - 4): ')

if level == '1':
	print('Easy')
elif level == '2':
	print('Medium')
elif level == '3':
	print('Hard')
elif level == '4':
	print('Expert')
else:
	print('Invalid level selected')
