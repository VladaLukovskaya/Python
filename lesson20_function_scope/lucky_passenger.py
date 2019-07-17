last_ticket = list('111112')  # 6-значное число

# если номер билета меньше 6-ти знаков, то надо как-то добавить в начало нули
def lucky(ticket):
    ticket_list = list(ticket)
    sum_1_this = int(ticket_list[0]) + int(ticket_list[1]) + int(ticket_list[2])
    sum_2_this = int(ticket_list[3]) + int(ticket_list[4]) + int(ticket_list[5])

    sum_1_last = int(last_ticket[0]) + int(last_ticket[1]) + int(last_ticket[2])
    sum_2_last = int(last_ticket[3]) + int(last_ticket[4]) + int(last_ticket[5])
    if sum_1_this == sum_2_this and sum_1_last == sum_2_last:
        print('The ticket is lucky.')
    else:
        print('The ticket is not lucky.')


lucky('123321')  # 6-значное число
