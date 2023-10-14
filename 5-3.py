username = input('Username: ')
password = input('Password: ')
if (username == 'admin' and password == '1234'):
	print(' User and Password is True ')
elif (username == 'admin' or password == '1234'):
	print(' User or Password is False ')
else:
	print('Invalid username or password.')
