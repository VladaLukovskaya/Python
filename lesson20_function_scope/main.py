# к внешним переменным через функцию прибегать не рекомендуется, \
# однако можно, если это константа и она используется не в одной функции

ENGLISH_RAINBOW_COLORS = [  # Immutables (константы) пишутся большими буквами
'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'
]
RUSSIAN_RAINBOW_COLORS = [
'красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий',
'фиолетовый'
]
def rainbow_color(index, russian_or_english):
    if russian_or_english == 'russian':
        print(RUSSIAN_RAINBOW_COLORS[index])
    elif russian_or_english == 'english':
        print(ENGLISH_RAINBOW_COLORS[index])
    else:
        print('Неверный язык')


rainbow_color(2, 'russian', '\n')


# area = 'Красная площадь'
#
#
# def print_square_area(length, width):
#     area = length * width
#     print('Площадь площади: ', area)
#
#
# print('Место встречи: ', area)
# print_square_area(330, 75)
# print('Повторяю, место встречи: ', area)


# при этом часто весь код внешнего уровня (те всё, что находится за пределами \
# функции) переносят в отдельную функцию main, чтобы не вносить в прогу лишние \
# глобальные переменные, а также для того, чтобы все переменные были локальными \
# и не загрязняли область видимости других функций:


def print_square_area(length, width):
    area = length * width
    print('Площадь площади: ', area)


def main():
    area = 'Красная площадь'
    print('Место встречи: ', area)
    print_square_area(330, 75)
    print('Повторяю, место встречи: ', area, '\n')


main()


# global variables
ask_number = 0


def ask_again(): # подсчёт кол-ва вызовов функции
    global ask_number
    ask_number = ask_number + 1
    print('Ты спрашиваешь меня уже в ', ask_number, '-й раз', sep='')


ask_again()
ask_again()
ask_again()
# однако следует помнить, что не рекомендуется использовать глобальные переменные внутри \
# функций, тем более, изменять их глобально


