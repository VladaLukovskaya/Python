string = input('Enter your string: ')
counter = 1
value = 0

if len(string) == 1:
    print(counter, string)
else:
    for elem in range(len(string)):
        value = string[elem]
        if elem + 1 == len(string):
            print(counter, value)
        elif string[elem] == string[elem + 1] :
            counter += 1
        elif string[elem] != string[elem + 1] and string[elem] == string[elem - 1]:
            print(counter, value)
            counter = 1
        else:
            counter = 1
            print(counter, value)
