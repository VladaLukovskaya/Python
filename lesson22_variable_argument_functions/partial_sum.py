def partial_sums(*args):
    sum = 0
    all_sums = []
    all_sums.append(sum)
    for elem in args:
        sum += elem
        all_sums.append(sum)
    print(all_sums)


partial_sums(1, 0.5, 0.25, 0.125)
