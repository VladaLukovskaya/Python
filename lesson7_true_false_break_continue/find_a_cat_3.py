number = 0
num_of_str = 0
flag = False
number_of_cats = 0

while number >= 0:  # либо до момента, пока не встретим "стоп"
    string = input()
    string = string.lower()
    number += 1
    if 'cat' in string and num_of_str != 0:
        number_of_cats += 1
        continue
    elif 'cat' in string:
        num_of_str = number
        number_of_cats += 1
        flag = True
    if 'stop' in string:
        break

if flag:
    print('The first string: ', num_of_str)
    print('All strings with cats: ', number_of_cats)
else:
    print(-1)
