from MiscFiles.library import *

ans = 0

starting_raw, gates_raw = get_input(2024, 24).split("\n\n")
swaps = {'rpv': 'z11', 'z11': 'rpv', 'ctg': 'rpb', 'rpb': 'ctg', 'z31': 'dmh', 'dmh': 'z31', 'dvq': 'z38', 'z38': 'dvq'}
starting_values = dict()
for line in starting_raw.split("\n"):
    line = line.split(": ")
    starting_values[line[0]] = (line[1] == '1')


def get_value(gate):
    global values
    if gate in values:
        return values[gate]
    print(gate, gates[gate])
    x, op, y = gates[gate]
    if op == "AND":
        left = get_value(x)
        right = get_value(y)
        values[gate] = left and right
    if op == "OR":
        left = get_value(x)
        right = get_value(y)
        values[gate] = left or right
    if op == "XOR":
        values[gate] = get_value(x) != get_value(y)
    return values[gate]


gates = dict()
gate_outputs = []
for line in gates_raw.split('\n'):
    line = line.split()
    output_gate = line[-1]
    if output_gate in swaps:
        output_gate = swaps[output_gate]
    gates[output_gate] = (line[0], line[1], line[2])
    gate_outputs.append(line[-1])
out = [x for x in gate_outputs if x.startswith('z')]
out.sort()


# Swaps found manually by looking at the output given below. Each output bit should
# have the same setup: It is fed by two intermediate gates XORed together. One intermediate
# gate is the two corresponding input bits XORed together and the other is the carry bit.
# The wrong gates are fairly obvious when I print the gates as I do below, and I can add
# them to swaps to see if that fixes it.
#
# To find the solution of an arbitrary output, clear swaps and re-derive it as I describe
# above.
values = starting_values.copy()
ans = ''
for o in out:
    print(o)
    ans += str(int(get_value(o)))
    print()

ans = ''.join(reversed(ans))
ans = int(ans, 2)

print("Part 1:", ans)
print("Part 2:", ','.join(sorted(list(swaps.keys()))))
