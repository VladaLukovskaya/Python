employees = list()
number = int(input('Enter the number of employees: '))

for strings in range(number):
    string = input()
    employees.append(string)
print('\n')

passwd = input('Enter simple passwords: ')
invalid_pass = passwd.split(';')

for strings in range(number):
    data = employees[strings].split(':')
    if data[1] in passwd:
        print('To:', data[0])
        print(data[4], ', your password is simple, change it.', sep='')
