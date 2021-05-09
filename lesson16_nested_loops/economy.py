# stations_number = int(input('Enter stations number:'))
stations_number = 4
# print('Enter path costs for all stations:')
paths_matrix = ['0', ['1'], ['2', '3'], ['4', '5', '6']]

# for row in range(stations_number - 1):
#     path_cost = input()
#     paths_matrix.append(path_cost.split(' '))

# print(paths_matrix)

all_paths = dict()
for station in range(stations_number - 1):
    station_number = station + 1
    # print('Number:', station)
    for paths in paths_matrix[station + 1:]:
        print(paths[station])
        # print('The station number:', station_number)
        all_paths[(station_number, station)] = paths[station]
        station_number += 1

print(all_paths)

first_stat, second_stat = tuple(map(int, input('Enter your path: ').split(' ')))

for key, value in all_paths.items():
    if first_stat in key:
        print(key)


#  use dictionary with key = path (ABC) and value = total cost of the path ?
