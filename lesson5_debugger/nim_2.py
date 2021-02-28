first_heap = int(input('Amount of stones in the first heap at the beginning: '))
second_heap = int(input('Amount of stones in the second heap at the beginning: '))

while first_heap != 0 or second_heap != 0:
    heap_number = int(input('The heap number: '))
    stones_number = int(input('Amount of taken stones: '))
    if heap_number == 1:
        first_heap -= stones_number
        print('Amount of stones in the first heap', first_heap, '\nAmount of stones in the first heap', second_heap)
    else:
        second_heap -= stones_number
        print('Amount of stones in the first heap', first_heap, '\nAmount of stones in the first heap', second_heap)
