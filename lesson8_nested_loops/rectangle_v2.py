columns = int(input('The number of columns: '))
strings = int(input('The number of strings: '))
symbol = input('Enter your symbol: ')
column = 0
string = 0

for string in range(strings):
    if string == 0 or string == strings - 1:
        for column in range(columns):
            print(symbol, end='')
    else:
        print(symbol, end='')
        for column in range(1, columns - 1):
            print(' ', end='')
        print(symbol, end='')
    print()
