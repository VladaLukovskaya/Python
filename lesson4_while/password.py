password = input('Enter your password: ')
check = input('Enter the password again: ')
correct = ''

while correct != 'OK':
    if len(password) < 8:
        print('The password is short.')
        new_password = input('Enter new password: ')
        password = new_password
        new_check = input('Enter new password again: ')
        check = new_check
    elif '123' in password:
        print('The password is simple.')
        new_password = input('Enter new password: ')
        password = new_password
        new_check = input('Enter new password again: ')
        check = new_check
    elif password != check:
        print('These passwords are different.')
        new_password = input('Enter new password: ')
        password = new_password
        new_check = input('Enter new password again: ')
        check = new_check
    else:
        correct = 'OK'
        print(correct)
