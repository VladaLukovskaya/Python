maximum = 1
new_max = 0
string = input('Enter your string: ')
new_str = ' '.join(string)
list = new_str.lower().split()

if len(string) == 1:
    print(maximum)
else:
    for elem in list:  # ищем букву, которая встречается чаще всего
        new_max = list.count(elem)
        if new_max > maximum:
            element = elem
            maximum = new_max
            new_max = 0
    print(maximum, element)
