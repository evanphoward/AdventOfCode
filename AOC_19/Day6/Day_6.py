planets = {}
reverse_planets = {}
i = 0


def total_orbit(p, count):
    if p == "COM":
        return count
    else:
        return total_orbit(planets[p], count) + 1


def search(node, length, seen):
    seen = seen.copy()
    if node in seen or node == "COM" or node not in reverse_planets.keys():
        return 100000
    if planets[node] == "SAN" or reverse_planets[node] == "SAN":
        return length
    seen.add(node)
    if node not in reverse_planets.keys():
        return search(planets[node], length + 1, seen)
    return min(search(planets[node], length + 1, seen), search(reverse_planets[node], length + 1, seen))


for line in open("input").readlines():
    inner, outer = line.strip().split(")")
    planets[outer] = inner
    reverse_planets[inner] = outer

total = 0
for planet in planets.keys():
    total += total_orbit(planet, 0)

print("Part One: ", total)
print("Part One: ", search(planets["YOU"], 0, set()))
