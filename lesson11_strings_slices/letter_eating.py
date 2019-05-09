string = input('Enter your string: ')
print(string)

while len(string) > 2:
    for symbol in string:
        string = string[1:len(string) - 1]
        print(string)
