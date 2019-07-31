def encrypt_caesar(message, shift):  # щифруем сообщение с заданным шагом
    encrypt_message = ''
    for letter in message:
        if (ord(letter) >= 65) and (ord(letter) <= 90) or \
                (ord(letter) >= 97) and (ord(letter) <= 122):  # является ли символ буквой латиницы
            if ((ord(letter) + shift) >= 65) and ((ord(letter) + shift) <= 90) or \
                    ((ord(letter) + shift) >= 97) and ((ord(letter) + shift) <= 122):
                encrypt_message += chr(ord(letter) + shift)
            else:
                encrypt_message += chr(ord(letter) + shift - 26)
        else:
            encrypt_message += letter
    return encrypt_message


def decrypt_caesar(message, shift):  # расшифровываем это сообщение
    decrypt_message = ''
    for letter in message:  # действия обратны функции шифрования
        if (ord(letter) >= 65) and (ord(letter) <= 90) or \
                (ord(letter) >= 97) and (ord(letter) <= 122):
            if ((ord(letter) - shift) >= 65) and ((ord(letter) - shift) <= 90) or \
                    ((ord(letter) - shift) >= 97) and ((ord(letter) - shift) <= 122):
                decrypt_message += chr(ord(letter) - shift)
            else:
                decrypt_message += chr(ord(letter) - shift + 26)
        else:
            decrypt_message += letter
    return decrypt_message


msg = 'abc Def Ghi ! # % xyZ'
space = 5

encrypted = encrypt_caesar(msg, space)
decrypted = decrypt_caesar(encrypted, space)

print(encrypted)
print(decrypted)
