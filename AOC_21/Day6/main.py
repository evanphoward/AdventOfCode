fish = list(map(int, open("input").readline().split(",")))
ages = [0] * 9
for f in fish:
    ages[f] += 1

for i in range(256):
    old_ages = ages
    ages = ages[1:] + [0]
    ages[6] += old_ages[0]
    ages[8] += old_ages[0]
    if i == 80:
        print("Part 1:", sum(ages))

print("Part 2:", sum(ages))
