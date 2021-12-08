from collections import defaultdict

min_presents = int(open("input").read())
house_values_1 = defaultdict(int)
house_values_2 = defaultdict(int)
for elf in range(1, min_presents // 10):
    house_counter = 0
    for house in range(elf, min_presents // 10, elf):
        house_counter += 1
        house_values_1[house] += 10 * elf
        if house_counter < 50:
            house_values_2[house] += 11 * elf

p1 = True
for num in range(min_presents // 10):
    if p1 and house_values_1[num] >= min_presents:
        print("Part 1:", num)
        p1 = False
    if house_values_2[num] >= min_presents:
        print("Part 2:", num)
        break
