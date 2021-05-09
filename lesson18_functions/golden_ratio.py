num = int(input('Enter the number: '))


def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


def golden_ratio(number):
    print(fibonacci(number + 1) / fibonacci(number))
    return fibonacci(number + 1) / fibonacci(number)


golden_ratio(num)
