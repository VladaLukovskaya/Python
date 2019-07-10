string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')

string_1 = string_1.lower()
string_2 = string_2.lower()

if string_1 == 'да' or string_1 == 'нет':
    if string_2 == 'да' or string_2 == 'нет':
        print('Верно')
    else:
        print('Неверно')
else:
    print('Неверно')
