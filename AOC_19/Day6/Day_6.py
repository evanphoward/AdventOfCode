planets = {}
neighbors = {}
i = 0


def total_orbit(p, count):
    if p == "COM":
        return count
    else:
        return total_orbit(planets[p], count) + 1


def search(node, length, seen):
    seen = seen.copy()
    if node in seen:
        return 1000000
    if "SAN" in neighbors[node]:
        return length
    seen.add(node)
    return min([search(plan, length + 1, seen) for plan in neighbors[node]])


for line in open("input").readlines():
    inner, outer = line.strip().split(")")
    planets[outer] = inner
    if inner not in neighbors.keys():
        neighbors[inner] = {outer}
    else:
        neighbors[inner].add(outer)
    if outer not in neighbors.keys():
        neighbors[outer] = {inner}
    else:
        neighbors[outer].add(inner)

total = 0
for planet in planets.keys():
    total += total_orbit(planet, 0)

print("Part 1:", total)
print("Part 2:", search(planets["YOU"], 0, set()))
