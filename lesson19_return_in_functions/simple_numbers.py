def prime(number):
    count = 0
    for num in range(1, round(number/2)+1):  # проверяем до середины всего списка \
        # возможных чисел, потому что больше нет смысла
        if number % num == 0:
            count += 1
    if count == 1:
        print("It's a simple number.")
    else:
        print("It's not a sipmle number.")


prime(8)
