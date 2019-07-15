# def golden_ratio():
#    number = int(input('Enter the number of fibonacci: '))
#    prev_number = int(input('Enter the previously number: '))
#    next_number = number + prev_number
#    ratio = next_number / number
#    return ratio

num = int(input('Enter the number: '))


def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 2) + fibonacci(number - 1)


def golden_ratio(number):
    return fibonacci(number + 1) / fibonacci(number)


print(golden_ratio(num))
