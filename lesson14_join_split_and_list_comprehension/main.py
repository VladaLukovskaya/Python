s = 'раз два три'
print(s.split() == ['раз', 'два', 'три'])
print('     one two  three  '.split() == ['one', 'two', 'three'])
print('192.168.1.1'.split('.') == ['192', '168', '1', '1'])
print(s.split('а') == ['р', 'з дв', ' три'])
print('A##B##C'.split('##') == ['A', 'B', 'C'], '\n')

s = ['Тот', 'Кого', 'Нельзя', 'Называть']
print(''.join(s) == 'ТотКогоНельзяНазывать')
print(' '.join(s) == 'Тот Кого Нельзя Называть')
print('-'.join(s) == 'Тот-Кого-Нельзя-Называть')
print('! '.join(s) == 'Тот! Кого! Нельзя! Называть', '\n')

# список квадратов чисел через цикл:
squares = list()
for i in range(10):
    squares.append(i**2)
print(squares, '\n')

# список квадратов через списочное выражение:
squares = [i ** 2 for i in range(10)]
print(squares, '\n')
# для чётных чисел:
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares, '\n')

# проходимся по двум циклам:
print([i * j for i in range(3) for j in range(3)], '\n')

evil, good = [int(x) for x in '666 777'.split()]
print(evil, good, sep='\n')
print('\n')

print(', '.join(str(i) + '^2=' + str(i**2) for i in range(1, 10)))

print('\nСписочные выражения также могут фильтровать список: ')
print([x for x in range(10) if x % 2 == 0 and x % 3 != 0])  # список чётных цифр, \
# не делящихся на 3


# преобразуем список слов двумя разными способамия:
words = ['В', 'новом', 'списке', 'останутся', 'только','длинные', 'слова']
long_words = list(map(lambda word: word.upper(),
filter(lambda word: len(word) > 6, words)))
long_words_lambda = [word.upper() for word in words if len(word) > 6]
print('\n', long_words, long_words_lambda)
