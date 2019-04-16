print('Enter your new code.')
first = input('First number: ')  # а если я здесь введу больше цифр
second = input('Second number: ')  # и вообще лучше вводить сразу трёхзначное
third = input('Third number: ')  # или здеь надо решать через mod и div

if first != second and first != third and second != third:
    print('Correct code.')
elif first == second and second == third:
    print('There are three identical numbers.')
elif first == second or first == third or second == third:
    print('There are two identical numbers.')
else:
    print('Incorrect code.')
