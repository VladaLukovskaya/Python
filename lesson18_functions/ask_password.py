import time


def ask_password():
    passw = input('Enter a password: ')
    real_pass = 'password'
    if passw == real_pass:
        return True
    else:
        return False


for elem in range(3):
    if ask_password():
        print('The password accepted.')
        break
    else:
        time.sleep(0.5)
        print('Access is denied.')
        if elem == 2:
            print('\nAttempts ended.')
