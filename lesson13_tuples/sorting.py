number = int(input('Enter: '))
numbers = []

for elem in range(number):
    numbers.append(int(input()))
for elem in range(number - 1):
    for elem_2 in range(number - 1 - elem):
        if numbers[elem_2] < numbers[elem_2 + 1]:
            numbers[elem_2], numbers[elem_2 + 1] = numbers[elem_2 + 1], numbers[elem_2]
print(numbers)
