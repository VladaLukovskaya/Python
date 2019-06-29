book = {}
value = ''

number = int(input('Enter the number of phone numbers: '))
print('Enter phone numbers and names in format "number name": ')

for elem in range(number):
    info = input()
    new_info = info.split()
    if new_info[1] in book:
        value = new_info[0] + ' ' + value
        value = value.split(' ')
        key = new_info[1]
    else:
        value = new_info[0]
        key = new_info[1]
    book[key] = value

request = ''
print('Enter your requests(if you want to stop looking for, write "end"): ')

while request != 'end':  # не нравится такое условие и конструкция
    request = input()
    if request == 'end':
        break
    if request in book:
        if type(book[request]) == list:
            print('Name: ', request, '. ', 'Phone number(s): ', ', '.join(book[request]), sep='')
        else:
            print('Name: ', request, '. ', 'Phone number(s): ', book[request], sep='')
    else:
        print('This name do not exist in the phone number.')
