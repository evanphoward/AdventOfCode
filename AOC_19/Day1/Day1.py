print("Part 1:", sum([int(x) // 3 - 2 for x in open("input").readlines()]))

total = 0
for mass in open("input").readlines():
    mass = int(mass)
    while mass > 0:
        mass = mass // 3 - 2
        if mass > 0:
            total += mass
print("Part 2:", total)
