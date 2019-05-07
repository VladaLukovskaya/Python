word = input('Enter your message: ')
number = int(input('Enter the number of letter: '))

if number <= len(word) and number > 0:
    print(word[number - 1])
else:
    print('Error.')