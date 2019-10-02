print(input)  # выведет инфу об инпуте
print(input())  # будет ждать ввод и выведет его

vyvod = print  # записали функцию принт в переменную, передав ей все возможности принта
vyvod('\nHi!')

# ------
# program 1:


def print_boxed(arr):
    arr_stringified = [str(element) for element in arr]
    mid = ' | '.join(arr_stringified)  # создаём строку с чертами между \
    # бывшими элементами списка
    bar = '-' * (2 + len(mid))  # len(mid) = 9
    print(' ' + bar + ' ')
    print('| ' + mid + ' |')
    print(' ' + bar + ' ')


def print_simple(arr):
    arr_stringified = [str(element) for element in arr]
    print(', '.join(arr_stringified))


formatting = 'boxed'

if formatting == 'boxed':
    print_formatted = print_boxed
else:
    print_formatted = print_simple

array = [1, 2, 3]

print_formatted(array)
print_formatted(['abc', 'def', 'ghi'])

# end of the program
# ------

print('\nФункции, которые принимают или возвращают другие функции, \
называются функциями высшего порядка.', end='\n\n')

# ------
# program 2:
# напишем прогу, фильтрующую слова по длине:


def is_word_long(word):
    return len(word) > 6


words = ['В', 'новом', 'списке', 'останутся', 'только',
        'длинные', 'слова']

for word in filter(is_word_long, words):  # сообщаем функции filter список и критерий отбора
    print(word)

print('\nОбъекты, которые можно перебирать циклом for - т.е. итерировать, называются итераторами.', end='\n\n')

# Через принт полученные элементы мы не получим, это можно сделать \
# с помощью такого способа:
long_words = list(filter(is_word_long, words))
print(long_words, '\n')

# ------

print('''Очень часто в качестве аргумента для функций высшего порядка часто мы хотим использовать совсем простую
функцию. Причем нередко такая функция нужна в программе только в одном месте, поэтому ей необязательно даже
иметь имя.
Такие короткие безымянные (анонимные) функции можно создавать инструкцией lambda <аргументы>: <выражение>
Такая инструкция создаст функцию, принимающую указанный список аргументов и возвращающую
результат вычисления выражения.''', end='\n\n')

# теперь записать условие мы можем так: lambda word: len(word) > 6
long_words_lambda = list(filter(lambda word: len(word) > 6, words))
print(long_words_lambda)

# если мы хотим использовать одну функцию несколько раз:
add = lambda x, y: x + y
add(3, 5)
add(1, add(2, 3))

print('\nВсе числа до 100, которые делятся на 12 с остатком 7: ')
print(list(filter(lambda x: x % 12 == 7, range(1, 100))))

print('\nФункция map принимает преобразование и применяет его ко всем числам: ')
print(list(map(lambda x: x ** 2, range(1, 10))))

