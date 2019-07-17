base = ['Лена Катомко', 'Вася Пупкин', 'Катя Дороженко', 'Никита Васильев']


def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту сейчас ищут.') # попробовала через f-строки

    def search_card():
        if name in base:
            number = base.index(name) + 1
            print('Ваша карта с номером {} найдена.'.format(number)) # форматирование строки \
            # через format
        else:
            print('Ваша карта в базе не найдена.')

    search_card()


hello('Ши')
