poem = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
phrases = poem.strip().split(' ')
all_syllables = list()
counter = list()

for phrase in phrases:
    vowels_in_phrase = list(filter(lambda letter: letter in vowels, phrase))
    all_syllables.append(vowels_in_phrase)

counter = [len(elem) for elem in all_syllables]
counter = set(counter)

if len(counter) == 1:
    print('Pam pam')
else:
    print('Pam param')


# or if you want to get it through the function, use it:
# def rhythm(strings):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'y']
#     phrases = strings.split(' ')
#     all_syllables = list()
#     for phrase in phrases:
#         current_vowels_counter = 0
#         for letter in phrase:
#             if letter in vowels:
#                 current_vowels_counter += 1
#         all_syllables.append(current_vowels_counter)
#     all_syllables = set(all_syllables)
#     if len(all_syllables) == 1:
#         print('Pam pam')
#     else:
#         print('Pam param')
