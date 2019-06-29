field = list()
size = size_of_field = int(input('Enter the size of field: '))
print('Enter the number of bacteria in each cell of field: ')

for column in range(size):
    rows = [int(elem) for elem in input().split()]
    field.append(rows)  # elements are string, not int
print(field)

drops = int(input('Enter the number of drops: '))

for elem in range(drops):
    print('Enter coordinates of drop: ')
    col, row = int(input()), int(input())
    if field[row][col] > 7:
        field[row][col] -= 8
    else:
        field[row][col] = 0

print('Your new field with bacteria: ')
print(field)

# how can i reduce the number of bacteria in other cells?