mem_1 = dict()
mem_2 = dict()
for line in open("input").readlines():
    line = line.strip()
    if line[:2] == "ma":
        bitmask = line.split(" ")[2]
    else:
        value = int(line.split(" ")[2])
        binary_string = "{0:b}".format(value)
        while len(binary_string) < len(bitmask):
            binary_string = "0" + binary_string
        binary_string = "".join([binary_string[i] if bitmask[i] == "X" else bitmask[i] for i in range(len(binary_string))])
        mem_1[line[line.index("[")+1:line.index("]")]] = int(binary_string, 2)

        address = int(line[line.index("[") + 1:line.index("]")])
        binary_string = "{0:b}".format(address)
        while len(binary_string) < len(bitmask):
            binary_string = "0" + binary_string
        binary_strings = [[binary_string[i] if bitmask[i] == "0" else bitmask[i] for i in range(len(binary_string))]]
        while any('X' in b for b in binary_strings):
            new_strings = list()
            for string in binary_strings:
                if 'X' not in string:
                    new_strings.append(string)
                    continue
                first_x = string.index('X')
                new_one = string.copy()
                new_one[first_x] = '1'
                new_two = string.copy()
                new_two[first_x] = '0'
                new_strings.extend([new_one, new_two])
            binary_strings = new_strings.copy()
        for string in binary_strings:
            mem_2[int(''.join(string), 2)] = int(line.split(" ")[2])

print("Part 1:", sum(mem_1.values()))
print("Part 2:", sum(mem_2.values()))