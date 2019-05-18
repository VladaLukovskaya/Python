num_of_items = int(input('Enter the number of items: '))
items = list()
print('Enter items: ')

for item in range(num_of_items):
    white_item = input()
    items.append(white_item)

num_of_request = int(input('Enter the number of requests: '))
requests = list()
print('Enter requests: ')

for request in range(num_of_request):
    one_request = input()
    requests.append(one_request)

print('Allowed items for requests: ')
for request in requests:
    for item in items:
        if request == item:
            print(request)
