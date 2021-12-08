import re
rules, medicine = open("input").read().split("\n\n")
rules = [line.split(" => ") for line in rules.split("\n")]

new_molecules = set()
total = 0
for rule in rules:
    for match in re.finditer(rule[0], medicine):
        new_molecules.add(medicine[:match.start()] + rule[1] + medicine[match.end():])

print("Part 1:", len(new_molecules))


medicine = medicine[::-1]
rules = {rule[1][::-1]: rule[0][::-1] for rule in rules}
total = 0
# Greedily substitute the rules in reverse on a reversed string
# This works because many patterns are *Ar, and are unimportant for parsing, so we consume as soon as possible
while medicine != "e":
    medicine = re.sub("|".join(rules.keys()), lambda x: rules[x.group()], medicine, 1)
    total += 1
print("Part 2:", total)
