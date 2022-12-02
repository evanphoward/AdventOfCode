elf_totals = [sum((map(int, elf.split("\n")))) for elf in open("input").read().split("\n\n")]
print("Part 1:", max(elf_totals))
print("Part 2:", sum(sorted(elf_totals)[-3:]))
