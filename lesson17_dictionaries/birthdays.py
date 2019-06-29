birthdays = {}

number = int(input('Enter the number of classmates: '))
print('Enter information about birthdays in format "name date month": ')

for elem in range(number):
    info = input()
    new_info = info.split()
    if new_info[2] in birthdays:
        birthdays[new_info[2]] = new_info[1] + ' - ' + new_info[0] + \
            ', ' + birthdays[new_info[2]]
    else:
        birthdays[new_info[2]] = new_info[1] + ' - ' + new_info[0]

request = ''
num_of_req = int(input('Enter the number of requests: '))

print('Enter your months: ')

for elem in range(num_of_req):
    request = input()
    if request not in birthdays:
        print('No birthdays in this month.')
    else:
        print(birthdays[request])
