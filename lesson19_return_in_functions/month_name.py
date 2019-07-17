def month_name(month, language):
    eng_months = {  # можно было просто через список и искать по индексу
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'july',
        '8': 'august',
        '9': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december'
    }
    rus_months = {
        '1': 'январь',
        '2': 'февраль',
        '3': 'март',
        '4': 'апрель',
        '5': 'май',
        '6': 'июнь',
        '7': 'июль',
        '8': 'август',
        '9': 'сентябрь',
        '10': 'октябрь',
        '11': 'ноябрь',
        '12': 'декабрь'
    }
    if 'en' in language:
        return eng_months.get(month, 'There is no month with this number.')
    elif 'ru' in language:
        return rus_months.get(month, 'There is no month with this number.')


print(month_name('8', 'english'))  # look for 8-th month in english
