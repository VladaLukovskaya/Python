def palindrome():
    string = input('Enter your raw: ')
    new_raw = list(string)  # делаем нашу строку списком
    rev_raw = list(string)  # создаём отдельный список для ревёрса
    rev_raw.reverse()    # ревёрсим, значение записывается в rev_raw
    if new_raw == rev_raw:
        return "It's a palindrome."
    else:
        return "It's not a palindrome."


print(palindrome())
