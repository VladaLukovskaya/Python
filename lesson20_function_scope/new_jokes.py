jokes = []


def print_only_new(message):
    global jokes
    if message not in jokes:
        jokes.append(message)
        print(message)


print_only_new('Joke 1')
print_only_new('Joke 12')
print_only_new('Joke 13')
print_only_new('Joke 14')
print_only_new('Joke 12')
