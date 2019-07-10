sheets = int(input('Enter the number of sheets: '))
students_1 = set()
students_2 = set()

for sheet in range(1, sheets + 1):
    num_of_surname = int(input('Enter the number of surnames: '))
    print('Enter all students in a class: ')
    if sheet == 1:
        for surname in range(1, num_of_surname + 1):
            student = input()
            students_1.add(student)
    else:
        for surname in range(1, num_of_surname + 1):
            student = input('')
            students_2.add(student)
        stud = students_1.intersection(students_2)
print(stud)

