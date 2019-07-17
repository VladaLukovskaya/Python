# изменения не затрагивают внешние объекты:
def list_of_squares(array):
    new_array = []
    for i in range(len(array)):
        new_array.append(array[i] ** 2)
    array = new_array
    print(array is new_array) # is показывает, привязаны ли переменные \
    # к одному и тому же объекту


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_squares(list)
print('No modified: ', list) # внутри функции мы записывали значения в другой объект, \
# к которому потом просто привязали array(list), но за пределами функции этого объекта \
# не существет, следовательно, наш array(list) остался привязан к внешнему объекту \
# (как я поняла)


# изменение значений объектов без использования global \
# (этот способ чуть лучше, чем глобализация переменных)

def convert_to_squares(array):  # вычисление квадратов чисел списка
    for i in range(len(array)):
        array[i] = array[i] ** 2


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
convert_to_squares(list)
print('With modified: ', list)

print('''\n\nИзменияемые объекты - списки, множества и словари.
Неизменяемые - числа, булевые значения, строки и кортежи.
Неизменяемые объекты называются иммутабельными.''')

a = 1
print('\n', id(a), sep='') # id объекта "число 1"
a += 1
print(id(a)) # id изменился, a - это объект другого числа

s = 'Hello'
print('\n', id(s), sep='') # id строки "Hello"
s += ' world'
print(id(s)) # id другого объекта - строки "Hello world"

s = [1, 2, 3]
print('\n', id(s), sep='') # id списка
s += [9, 8, 7]
print(id(s), '\n') # тот же id для того же списка, но с измененным содержимым

my_fridge = ['молоко', 'яйца', 'овощи']
my_friends_fridge = ['молоко', 'яйца', 'овощи']
print('Equality:', my_fridge == my_friends_fridge)
print('ID:', id(my_fridge) == id(my_friends_fridge), '\n')  # содержимое идентично, но объекты разные

my_fridge = ['молоко', 'яйца', 'овощи']
my_parents_fridge = my_fridge
print('Equality:', my_fridge == my_parents_fridge)
print('ID:', id(my_fridge) == id(my_parents_fridge))

my_parents_fridge += ['мясо']
print("My fridge after modified my parents' fridge: ", my_fridge, '\n')

# если мы хотим получить только копию списка:
arr = [1, 2, 3]
arrCopy = arr[:]
arrCopy[0] = 42
print('Array:', arr) # => [1, 2, 3]
print('Copy of array with new element: ', arrCopy) # => [42, 2, 3]

# но(!) если список содержит вложенные списки, то при изменении в нём изменятся и \
# вложенные списки в источнике (аналогично с кортежами)
# также для изменяемых объектов в случае использования оператора а += б в первому объекту \
# в конец добавится второй(те мы измняем первый объект), \
# а при а = а + б запишется новый объект
