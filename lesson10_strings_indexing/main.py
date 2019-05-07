fixed_word = 'опять'
print(fixed_word, '\n')

word = input()
print(word, '\n')

number = 25
number_string = str(number)  # преобразовали число в строку
print(number_string, '\n')

word_plus_number = fixed_word + number_string
print(word_plus_number)
print(len(word_plus_number))
print('оп' in word_plus_number, '\n')

word = 'привет'
initial_letter = word[0]
print(initial_letter, '\n')  # сделает то же, что print('п')

word = 'привет'
number_of_letter = int(input())  # пользователь вводит число
print(word[number_of_letter])  # затем это число становится индексом

text = 'hello, my dear friends!'
vowels = 0
for letter in text:  # перебираем все буквы
    if letter in {'a', 'e', 'i', 'o', 'u', 'y'}:  # среди них ищем гласные
        vowels += 1
print(vowels)

text = 'hello, my dear friends!'
vowels = 0
for i in range(len(text)):
    if text[i] in 'aeiouy':  # то же через индексы
        vowels += 1
print(vowels)
