number = int(input('Enter the number: '))
count = 0

if number % 2 == 1 and number != 1:
    print('The number is odd')
elif number == 1:
    print('Yes. The degree is 0.')
else:
    while number > 0 and number % 2 != 1:
        number /= 2
        count += 1
    print('Yes. The degree is', count)


