pratice = 'if you have some message about pratice python_work please write here:'
pratice += '\n when write emmmmsomething to stope'
active = True
while active:
	message = input(pratice)
	if message == 'quit':
		active = False
	elif message == 'emmm':   
		active = False
	else:
		print(message)