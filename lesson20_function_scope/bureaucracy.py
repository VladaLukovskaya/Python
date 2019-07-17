def setup_profile(emp_name, dates_of_vac):
    global name, vacation_dates
    name = emp_name
    vacation_dates = dates_of_vac


def print_application_for_leave():
    print('Заявление на отпуск в период ', vacation_dates, '. ', name, sep='')


def print_holiday_money_claim(amount):
    print('Прошу выплатить ', amount, ' отпускных. ', name, sep='')


def print_attorney_letter(to_whom):
    print('На время отпуска в период ', vacation_dates, ' моим заместителем назначается ',
          to_whom, '. ', name, sep='')


def main():
    setup_profile('Ivan', 'june 2 - july 2')
    print_application_for_leave()
    print_application_for_leave()
    print_holiday_money_claim('15k')
    print_attorney_letter('Natalia')


main()
