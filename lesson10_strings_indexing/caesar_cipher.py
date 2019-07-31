step = int(input('Enter a number: '))
message = input('Enter your message: ')
new_message = ''

for letter in message:
    if (ord(letter) >= 65) and (ord(letter) <= 122):
        if (ord(letter) >= 91) and (ord(letter) <= 96) or (ord(letter) == 32):
            new_message += letter  # все "небуквы" оставляем неизменными
        elif ord(letter) + step <= 122:
            new_message += chr(ord(letter) + step)
        else:  # если эта латинская буква с прибавкой выходит за диапазон:
            new_message += chr(ord(letter) + step - 26)
    else:
        new_message += letter
print(new_message)
