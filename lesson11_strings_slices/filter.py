number = int(input('Enter the number of strings: '))

for num in range(number):
    print('Enter your strings: ')
    string = input()
    if string[:2] == '%%':
        print(string[2:])
    elif string[:4] == '####':
        continue
    else:
        print(string)