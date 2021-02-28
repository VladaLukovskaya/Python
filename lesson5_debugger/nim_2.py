first = int(input('Начальное количество камней в первой куче: '))
second = int(input('Начальное количество камней во второй куче: '))
while first != 0 or second != 0:
    n = int(input('Номер кучи: '))
    c = int(input('Количество забираемых камней: '))
    if n == 1:
        first -= c
        print(first, second)
    else:
        second -= c
        print(first, second)
