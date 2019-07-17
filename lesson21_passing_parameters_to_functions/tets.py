my_fridge = ['молоко', 'яйца', 'овощи']
my_parents_fridge = my_fridge
print(my_fridge == my_parents_fridge)
print(id(my_fridge) == id(my_parents_fridge))


arr = [2, 90, 5]
print(arr, arr.sort(), arr, sep='\n')
print('\n')

x = 1


def double_x():
    global x
    x *= 2


print(x, double_x(), x, sep='\n')
