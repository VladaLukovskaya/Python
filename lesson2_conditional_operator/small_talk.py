answer = input('Приветсвую! Как Ваше настроение? ')
answer = answer.lower()

if 'не ' in answer:
    print('Кажется, я не очень хорошо понимаю Ваш ответ.')
elif 'плох' in answer:
    print('Ничего, думаю, скоро у Вас всё наладится.')
elif 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
    print('Это прекрасно! У меня тоже всё хорошо)')
else:
    print('Кажется, я не очень хорошо понимаю Ваш ответ.')
