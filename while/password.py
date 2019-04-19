password = input('Enter your password: ')
check = input('Enter the password again: ')

if len(password) < 8:
    print('The password is short.')
elif '123' in password:
    print('The password is simple.')
elif password != check:
    print('These passwords are different.')
else:
    print('OK.')