number = 0
num_of_str = 0
flag = False

while number >= 0:  # либо до момента, пока не встретим "стоп"
    string = input()
    string = string.lower()
    number += 1
    if 'cat' in string and num_of_str != 0:
        continue
    elif 'cat' in string:
        num_of_str = number
        flag = True
    if 'stop' in string:
        break

if flag:
    print(num_of_str)
else:
    print(-1)
