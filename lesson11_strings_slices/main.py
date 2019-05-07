text = 'Hello, world!'
print(text[:5])
print(text[7:], '\n')

full_name = 'Иванов И. И.'
surname = full_name[:-6]
print(surname, '\n')

number = input('Enter: ')
odd = even = 0
# срез будет от начала строки до конца с шагом два: 0, 2, 4,...
for n in number[::2]:
    odd += int(n)
    # срез от второго элемента строки до конца с шагом два: 1, 3, 5,...
for n in number[1::2]:
    even += int(n)
if odd == even:
    print('Счастливый по-питерски!', '\n')
else:
    print('Счастливый, но не по-питерски)', '\n')

text = 'СЕЛ В ОЗЕРЕ БЕРЕЗОВ ЛЕС'
text_reversed = text[::-1]
print(text == text_reversed)
print(text_reversed)
