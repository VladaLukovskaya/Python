def my_sum(arr):
    result = 0
    for element in arr:
        result += element
    return result


print(my_sum([1, 2, 3, 4]), '\n')


def my_abs(x):  # модуль числа
    if x >= 0:
        return x
    else:
        return -x


def matrix_has_close_value(matrix, value, eps):  # проверяем, есть ли в матрице элемент, \
    # отличающийся от искомого не более, чем на eps
    for row in matrix:
        for cell in row:
            if abs(cell - value) <= eps:
                return True
    return False


table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = matrix_has_close_value(table, 3.75, 0.5)
print(result, '\n')


def get_coordinates():  # возврат нескольких значений (кортеж)
    return 1, 2


print(get_coordinates(), '\n')


# такие значения можно получить двумя способами:
result = get_coordinates()
print(result, '\n')

x, y = get_coordinates()
print(x) # => 1
print(y) # => 2
