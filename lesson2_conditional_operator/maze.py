print('Вы находитесь в заброшенном санатории. Вам необходимо найти выход.')
choice_1 = input('Перед вами три двери: красная, черная и белая. Напишите, какую вы выбираете: ')

if 'красн' in choice_1:
    right_choice = input('Вы открыли красную дверь и видите перед собой две лестницы. Вы выбираете правую или левую? ')
    right_choice = right_choice.lower()
    if 'прав' in right_choice:
        print('Вы выбрали правую лестницу и выбрались из санатория. Поздравляем!')
    else:
        print('Вы выбрали левую лестницу и попали в западню голодных оборотней.')
else:
    choice_2 = input('Вы выбрали дверь и попали в длинный коридор. Повернёте направо или налево? ')
    print('Вы долго шли по коридору и зашли в тупик.')
