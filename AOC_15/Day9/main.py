from collections import defaultdict
from itertools import permutations

cities = defaultdict(dict)
for line in open("input").readlines():
    line = line.split()
    cities[line[0]][line[2]] = int(line[4])
    cities[line[2]][line[0]] = int(line[4])

city_list = list(cities.keys())
distances = set()
for order in permutations(list(range(len(city_list)))):
    distances.add(sum(cities[city_list[order[i]]][city_list[order[i + 1]]] for i in range(len(city_list) - 1)))
print("Part 1:", min(distances))
print("Part 2:", max(distances))
