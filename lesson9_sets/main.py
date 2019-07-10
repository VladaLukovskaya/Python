amimals_and_numbers = {'cat', 5, 'dog', 3, 'fox', 12, 'elephant', 4}
print(amimals_and_numbers, '\n')

my_set = {'a', 'b', 'c'}
for elem in my_set:
    print(elem)
print('\n')

new_elem = 'e'
my_set.add(new_elem)
print(my_set, '\n')  # добавляем новый элемент
# удаляем элементы:
my_set.discard('a')         # Удалён
my_set.discard('hello')     # Не удалён, ошибки нет
my_set.remove('b')          # Удалён
print(my_set, '\n')               # В множестве остался один элемент 'c'
my_set.remove('world')      # Не удалён, ошибка KeyError

s1 = {'a', 'b', 'c'}
s2 = {'a', 'c', 'd'}
union = s1.union(s2)                      # {'a', 'b', 'c', 'd'} - есть хотя бы в одном
intersection = s1.intersection(s2)        # {'a', 'c'} - есть в обоих множествах
diff = s1.difference(s2)                  # {'b'} - есть в первом, но не во втором (s1 - s2)
symm_diff = s1.symmetric_difference(s2)   # {'b', 'd'} - есть только в одном из них (s1 ^ s2)
