import string
import secrets


def generate_password(letters_num, alphabet):
    digit = string.digits
    lower_letter = string.ascii_letters.lower()
    upper_letter = string.ascii_letters.upper()
    counter = set()
    while counter != set('dlu'):
        password = ''.join(secrets.choice(alphabet) for i in range(letters_num))
        for letter in password:
            if letter in digit:
                counter.add('d')
            elif letter in lower_letter:
                counter.add('l')
            elif letter in upper_letter:
                counter.add('u')
    return password


def main(passwords_number, letters_number):
    original_alphabet = string.ascii_letters + string.digits
    chars_to_remove = 'oO0lI1'
    new_alphabet = original_alphabet

    for char in chars_to_remove:
        new_alphabet = new_alphabet.replace(char, '')

    passwords_list = list()
    for i in range(passwords_number):
        passwords_list.append(generate_password(letters_number, new_alphabet))
    return [passwords_list[0], passwords_list]


letters = 10
passwords = 5

print(f'A random password of {letters} characters: {main(passwords, letters)[0]}')
print(f'{passwords} random passwords of {letters} characters:')
for password in main(passwords, letters)[1]:
    print(password)
