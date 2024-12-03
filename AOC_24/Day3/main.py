from MiscFiles.library import *

inp = ''.join(get_input(2024, 3).split("\n"))
good = True
p1, p2 = 0, 0
for i in range(len(inp)):
    mult = re.match('^mul\((\d{1,3}),(\d{1,3})\)', inp[i:])
    if re.match('^do\(\)', inp[i:]):
        good = True
    if re.match("^don't\(\)", inp[i:]):
        good = False
    if mult:
        result = int(mult.group(1)) * int(mult.group(2))
        p1 += result
        p2 += result * good

print("Part 1:", p1)
print("Part 2:", p2)
