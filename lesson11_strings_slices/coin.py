results = input('Enter all results (h or t): ')
maximum = 0
new_max = 0

for result in results[:]:
    if result == 'h':
        maximum += 1
        if new_max < maximum:
            new_max = maximum
    else:
        maximum = 0
print(new_max)
