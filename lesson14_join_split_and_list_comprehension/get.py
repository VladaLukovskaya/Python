url = input('URL: ')
key = input('The key you are looking for: ')

first_split = url.split('?')
url = first_split[1]
second_split = url.split('&')

for parts in second_split:
    part = parts.split('=')
    if part[0] == key:
        print(part[1])