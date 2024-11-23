from MiscFiles.library import *

inp = get_input(2023, 2).split("\n")
inp = [[y.split() for y in x.split(";")] for x in inp]
p1, p2 = 0, 0

for idx, x in enumerate(inp):
    possible = True
    max_green, max_red, max_blue = 0, 0, 0
    for bag in x:
        green, red, blue = 0, 0, 0
        for j, elt in enumerate(bag):
            if elt.isdigit():
                if bag[j + 1].startswith("green"):
                    green = int(elt)
                elif bag[j + 1].startswith("red"):
                    red = int(elt)
                elif bag[j + 1].startswith("blue"):
                    blue = int(elt)
        max_green = max(max_green, green)
        max_red = max(max_red, red)
        max_blue = max(max_blue, blue)
        if red > 12 or green > 13 or blue > 14:
            possible = False

    if possible:
        p1 += (idx + 1)
    p2 += (max_green * max_red * max_blue)

print("Part 1:", p1)
print("Part 2:", p2)