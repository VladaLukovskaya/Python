Sveta = input('Что делает Света? ')
if 'готов' in Sveta:
    Vlad = 'доволен'
elif 'ест' or 'куш' in Sveta:
    Vlad = 'счастлив'
else:
    Vlad = 'не доволен'
print('Влад', Vlad)