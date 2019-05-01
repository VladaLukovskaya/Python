people = int(input('The number of people:'))
average = 0
all_iq = 0

for i in range(people):
    iq = int(input('Your IQ:'))
    all_iq += iq
    average = all_iq/(i + 1)
    if iq == average or i == 0:
        print('0')
    elif iq > average:
        print('>')
    else:
        print('<')
