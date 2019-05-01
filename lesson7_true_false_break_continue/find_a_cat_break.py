strings = int(input('Enter the number of strings: '))
flag = True

for i in range(strings):
    str = input()
    if 'cat' in str:
        print('Meow')
        flag = False
        break
if flag:
    print('There is no cat.')