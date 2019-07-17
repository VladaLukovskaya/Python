def print_goodbye():
    print('Goodbye,', end=' ')


def print_cruel(arg):
    print('cruel', end=' ')


def print_world(arg):
    print('world!', end=' ')


def main():
    print_world(print_cruel(print_goodbye()))  # вывод: Goodbye, cruel world!


main()
