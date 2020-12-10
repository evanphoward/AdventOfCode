from AOC_19.IntComputer import IntProcess

print("Part 1:", sum([IntProcess(open("input")).run([x, y])[0] for x in range(50) for y in range(50)]))

x = y = 0
while not IntProcess(open("input")).run([x+99, y])[0]:
    y += 1
    while not IntProcess(open("input")).run([x, y+99])[0]:
        x += 1
print("Part 2:", x*10000 + y)
