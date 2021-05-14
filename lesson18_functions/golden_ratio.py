def fibonacci(number):
    if number < 2:
        return number
    else:
        return fibonacci(number - 2) + fibonacci(number - 1)


def golden_ratio(number):
    print(fibonacci(number + 1) / fibonacci(number))
    return fibonacci(number + 1) / fibonacci(number)

