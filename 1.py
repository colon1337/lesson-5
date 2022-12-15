def pas():
	if len(a) < 6:
		print('Короткий пароль!')
	elif a.lower()=='password':
	    print('Пароль простой!')
	elif not any(b.isalpha() for b in a):
	    print('Пароль не должен состоять только из цифр!')
	elif not any(b.isdigit() for b in a):
		print('Пароль не должен состоять только из букв!')
	else:
	    print('Пароль верный!')
a=input('Введите пароль:')
pas()
