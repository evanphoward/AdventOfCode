inp = [x.split(",") for x in open("input").read().strip().split("\n")]

p1, p2 = 0, 0
for elf_1, elf_2 in inp:
    elf_1, elf_2 = list(map(int, elf_1.split("-"))), list(map(int, elf_2.split("-")))
    elf_1, elf_2 = set(range(elf_1[0], elf_1[1] + 1)), set(range(elf_2[0], elf_2[1] + 1))
    overlap = len(elf_1.intersection(elf_2))
    if overlap:
        p2 += 1
        if overlap == min(len(elf_1), len(elf_2)):
            p1 += 1

print("Part 1:", p1)
print("Part 2:", p2)
