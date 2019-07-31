# если кол-во переменных и значений не совпадает, то возникнет ошибка, \
# избежать этого можно, присвоив нескольок значений одной переменной:
x, y, *rest = 1, 2, 3, 4, 5, 6  # в данном случае rest всегда будет списком
print(rest, '\n')

# ещё примеры:
# x, y, *rest = 1, 2
# print(rest)
# => []

# x, y, z, *rest = 1, 2
# Ошибка выполнения


# звёздочка мржет быть только у одного аргумента, но необязательно последнего:
*names, surname = 'Анна Мария Луиза Медичи'.split()
print(names)
print(surname, '\n')

a, (b, c), d = [1, [2, 3], 4]  # возможность распаковать вложенные списки

# для распаковки кортежа из одного элемента используется запятая после переменной:
n = (1,)
m, = (1,)
print(n)  # => (1,), те присвоился весь кортеж
print(m, '\n')  # => 1

print('''Важно: при множественном присваивании переменная со звёздочкой получает 
список значений, в случае с аргументом функции под звёздочкой получаем кортеж.''', '\n')


def product(first, *other):  # вычисляем произведение аргументов
    result = first
    for value in other:
        result *= value
    return result


print(product(2, 3, 5, 7), '\n')


arr = ['cd', 'ef', 'gh']
print(*arr)
# Раскрытие списка можно комбинировать с любыми аргументами
print('ab', *arr, 'yz')  # => ab cd ef gh yz
# При раскрытии может быть несколько аргументов со звездочкой
print(*arr, ',', *arr)  # => cd ef gh cd ef gh
print('\n')


def make_burger(type_of_meat, with_onion=False, with_tomato=True):  # первыми указываем более важные значения
    print('Булочка')
    if with_onion:
        print('Луковые колечки')
    if with_tomato:
        print('Ломтик помидора')
    print('Котлета из', type_of_meat)
    print('Булочка')


print("Vanya's burger: ")
make_burger("свинины", True)
print('\nOther burger: ')
make_burger("свинины", False, False)
print('\n')


def profile(name, surname_2, city, *children, **additional_info):  # те все \
    # позиционные аргументы будут в переменной с одной звёздочкой, а все \
    # именованные - в аргументе с двумя
    print("Имя:", name)
    print("Фамилия:", surname_2)
    print("Город проживания:", city)
    if len(children) > 0:
        print("Дети:", ", ".join(children))
    print(additional_info)


profile("Сергей", "Михалков", "Москва", "Никита Михалков",
        "Андрей Кончаловский", occupation="writer", died_in=2009)
print('\n')

print(['Массив', 'из', 'четырех', 'аргументов'])
# => ['Массив', 'из', 'четырех', 'аргументов']
print(*['Просто', 'три', 'аргумента'], '\n')
# => Просто три аргумента

# две звёздочки позволяют нам так же распаковать и словарь

def perforated_print(*args, **kwargs):
    print(*args,**kwargs)  # передаём все полученные аргументы в функцию принт
    print('-' * 20)


perforated_print('Теперь текст выводится с линией перфорации.')
perforated_print('И', 'можно', 'использовать', 'опции', end=':\n')
perforated_print('end', 'sep', 'и прочие', sep=', ', end='!\n')
