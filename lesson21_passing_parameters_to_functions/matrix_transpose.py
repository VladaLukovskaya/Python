matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def transpose(matrix):
    return [list(elem) for elem in zip(*matrix)]  # zip создаёт из нескольких \
    # списков новый список кортежей, где в первом кортеже находятся все первые \
    # элементы списков, во втором - вторые и тд
    # * в zip как бы распаковывает наш список, используя каждый из его элементов \
    # как отдельный объект

    # либо через обычный for
    # new_matrix = []
    # for elem in zip(*matrix):
    #     new_matrix.append(list(elem))
    # return new_matrix

print(transpose(matrix))
