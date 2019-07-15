def palindrome(raw):
    new_raw = list(raw)  # делаем нашу строку списком
    rev_raw = list(raw)  # создаём отдельный список для ревёрса
    rev_raw.reverse()    #  ревёрсим, значение записывается в rev_raw
    if new_raw == rev_raw:
        return "It's a palindrome."
    else:
        return "It's not a palindrome."


string = input('Enter your raw: ')
print(palindrome(string))
