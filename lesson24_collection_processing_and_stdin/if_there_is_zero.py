from sys import stdin

print(any(list([True for elem in stdin.read().replace('\n', ' ').split(' ') if elem == '0'])))
