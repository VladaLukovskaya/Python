strings = int(input('Enter the number of strings: '))
flag = True

for i in range(strings):
    string = input()
    if 'cat' in string:
        print('Meow')
        flag = False
        break
if flag:
    print('There is no cat.')
