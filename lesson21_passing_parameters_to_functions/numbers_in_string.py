list = [1, 2, 3]


def from_string_to_list(string, container):
    new_string = string.split(' ')
    for elem in new_string:
        container.append(int(elem))  # извлекаем числа из строки и добавляем в список
    print(container)


# from_string_to_list('4 5 6', list)
