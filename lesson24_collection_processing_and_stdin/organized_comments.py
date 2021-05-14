from sys import stdin

map_lines = list(map(lambda line: line, stdin.read().split('\n')))
comments = [(line.strip('#').strip(), map_lines.index(line) + 1) for line in map_lines if '#' in line]

for comment, line_number in comments:
    print(f'Line {line_number}: {comment}')
