a = 0  # нижняя граница интервала
b = 1000  # верхняя граница интервала
medium = (a+b)/2
print(medium)
answer = 1001

while answer != '=':
    answer = input()
    if answer == '<':
        b = medium
        medium = (a+b)/2
        if medium % 2 != 0:
            medium += 1
        print(medium)
    else:
        a = medium
        medium = (a+b)/2
        print(medium)
        if medium % 2 != 0:
            medium += 1
print('I guessed it!')