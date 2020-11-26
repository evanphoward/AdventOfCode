paper = 0
ribbon = 0
for box in open("input").readlines():
    sides = box.split("x")
    areas = list()
    areas.append(int(sides[0])*int(sides[1]))
    areas.append(int(sides[0]) * int(sides[2]))
    areas.append(int(sides[1]) * int(sides[2]))
    paper += 2*sum(areas) + min(areas)

    ribbon += int(sides[0]) * int(sides[1]) * int(sides[2])
    if areas.index(min(areas)) == 0:
        ribbon += 2*int(sides[0]) + 2*int(sides[1])
    if areas.index(min(areas)) == 1:
        ribbon += 2*int(sides[0]) + 2*int(sides[2])
    if areas.index(min(areas)) == 2:
        ribbon += 2*int(sides[1]) + 2*int(sides[2])


print("Part 1:", paper, "\nPart 2:", ribbon)