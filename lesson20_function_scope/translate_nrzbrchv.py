translated_text = None


def translate(text):
    global translated_text
    letters = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с',
               'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'Б', 'В', 'Г',
               'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С',
               'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', ' ']
    text = list(text)
    output = []
    for letter in text:
        if letter in letters:
            output.append(letter)
            translated_text = ''.join(output)
    print(translated_text)


translate('йцукен ПРРПщщз хъп авы фячсмитьбю.орлы?')
