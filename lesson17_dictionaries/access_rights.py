ways = {}

num_of_permission = int(input('Enter the number of permission folders: '))
print('Enter permissions:')

for elem in range(num_of_permission):
    permission = input()
    folder = permission.split('/')
    count = 2
    for element in folder[1::]:  # пытаюсь сделать каждую папку ключом,
        # но чтобы в нём были все разрешённые внутренние папки в значениях
        if count <= len(folder):
            ways[element] = folder[count]
            count += 1
    print(ways)
print(folder)