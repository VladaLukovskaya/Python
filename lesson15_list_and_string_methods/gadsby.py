letter = input('Enter the forbidden letter: ')
string = input('Enter your text: ')
list = string.split()

for elem in list:
    if letter in elem:
        print(elem)