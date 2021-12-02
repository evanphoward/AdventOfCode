inp = [line.split() for line in open("input").readlines()]
pos = sum(int(line[1]) if line[0] == "forward" else 0 for line in inp)
depth = sum(int(line[1]) if line[0] == "down" else -int(line[1]) if line[0] == "up" else 0 for line in inp)
print("Part 1:", pos * depth)

depth = 0
aim = 0

for line in inp:
    if line[0] == "forward":
        depth += aim * int(line[1])
    else:
        aim += int(line[1]) if line[0] == "down" else -int(line[1])

print("Part 2:", pos * depth)
