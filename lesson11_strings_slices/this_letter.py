string = input('Enter your string: ')
number = int(input('Enter your favorite number: '))
letter = input('Enter your favorite letter: ')

for letters in string[:]:
    if string[number] and (number <= len(string) or number < 0):
        if len(letter) == 1:
            if string[number - 1] == letter:
                print('Yes.')
            else:
                print('No.')
    else:
        print('Error.')
