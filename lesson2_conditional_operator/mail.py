login = input('Введите логин: ')
email = input('Введите адрес эл. почты: ')

if '@' not in login and '@' in email:
    print('Correct')
elif '@' in login:
    print('Incorrect login')
elif '@' not in email:
    print('Incorrect email')
else:
    print('I do not know how you did it.')
