for i in range(17):
    number = int(input('Enter a number:'))
    if i % number == 0:
        print('Yes')
    else:
        print('No')
    i += 1
