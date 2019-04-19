number = int(input('Enter a number: '))
count = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
        count += 1
    else:
        number = 3*number + 1
        count += 1
print(count)