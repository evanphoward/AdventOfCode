from MiscFiles.library import *

keypad =  {'7':(0, 0),  '8': (0, 1), '9': (0, 2), \
           '4': (1, 0), '5': (1, 1), '6': (1, 2), \
           '1': (2, 0), '2': (2, 1),  '3': (2, 2), \
                        '0': (3, 1), 'A': (3, 2)}
directional_pad = {             '^': (0, 1), 'A': (0, 2), \
                   '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
deltas = {'^': DIRS[0], '>': DIRS[1], 'v': DIRS[2], '<': DIRS[3]}

def path_hits_forbidden(pos, path, forbidden):
    for direction in path:
        if direction == 'A':
            continue
        dr, dc = deltas[direction]
        pos = (pos[0] + dr, pos[1] + dc)
        if pos == forbidden:
            return True
    return False

@functools.lru_cache()
def complexity(code, depth, limit):
    buttons = keypad if depth == 0 else directional_pad
    pos = buttons['A']
    length = 0
    for input_key in code:
        r, c = buttons[input_key]
        dr = r - pos[0]
        dc = c - pos[1]
        up_down = ('v' * abs(dr) if dr > 0 else '^' * abs(dr))
        left_right = ('>' * abs(dc) if dc > 0 else '<' * abs(dc))
        options = [up_down + left_right + 'A', left_right + up_down + 'A']
        options = [option for option in options if not path_hits_forbidden(pos, option, (3, 0) if depth == 0 else (0, 0))]
        if depth == limit:
            length += len(options[0])
        else:
            complexities = [complexity(option, depth + 1, limit) for option in options]
            length += min(complexities)
        pos = buttons[input_key]
    return length


inp = get_input(2024, 21).split("\n")
p1, p2 = 0, 0
for code in inp:
    p1 += (int(code[:-1]) * complexity(code, 0, 2))
    p2 += (int(code[:-1]) * complexity(code, 0, 25))

print("Part 1:", p1)
print("Part 2:", p2)