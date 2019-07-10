num_of_strings = int(input('Enter the number of strings: '))
strings = 0
cat = False

for strings in range(num_of_strings):
    string = input()
    string = string.lower()
    if 'cat' in string :
        cat = True
if cat:
    print('Meow')
