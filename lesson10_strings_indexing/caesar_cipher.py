step = int(input('Enter a number: '))
message = input('Enter your message: ')
new_message = ''

for letter in range(len(message)):
    new = ''
    new_letter = message[letter]
    if (ord(new_letter) + step) <= 122:
        new += chr(ord(new_letter) + step)
        new_message += new  # как сделать пробелы для разных слов?
    else:
        new += chr(ord(new_letter) + step - 26)
        new_message += new
print(new_message)
