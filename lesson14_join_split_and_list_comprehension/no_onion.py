number = int(input('Enter the number of strings: '))
recipe = list()

print('Enter your recipe: ')
for string in range(number):
    strings = input()
    if 'onion' in strings:
        continue
    else:
        recipe.append(strings)
print(', '.join(recipe))
