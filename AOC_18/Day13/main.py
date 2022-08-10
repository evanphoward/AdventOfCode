from functools import cmp_to_key

def print_carts(cts):
    cart_pos = dict()
    for r, c, heading, _ in cts:
        cart_pos[(r, c)] = heading
    for r in range(65, 75):
        for c in range(5, 15):
            if (r, c) in cart_pos:
                print(['^', '>', 'v', '<'][cart_pos[(r, c)]], end='')
            else:
                print(map[r][c], end='')
        print()
    print()

map = open("input").read().split("\n")
WIDTH = len(map[0])
HEIGHT = len(map)
carts = []
for r in range(HEIGHT):
    for c in range(WIDTH):
        if map[r][c] == '^':
            carts.append((r, c, 0, 0))
        elif map[r][c] == '>':
            carts.append((r, c, 1, 0))
        elif map[r][c] == 'v':
            carts.append((r, c, 2, 0))
        elif map[r][c] == '<':
            carts.append((r, c, 3, 0))

correct_mapping = {'|': '|', '-': '-', '/': '/', '\\': '\\', '^': '|', 'v': '|', '<': '-', '>': '-', ' ': ' ', '+': '+'}
map = [[correct_mapping[cell] for cell in line] for line in map]
heading_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    new_carts = []
    pos_occupied = set()
    for r, c, heading, turn in carts:
        dr, dc = heading_delta[heading]
        r += dr
        c += dc
        if map[r][c] == '/':
            heading = 3 - ((heading + 2) % 4)
        elif map[r][c] == '\\':
            heading = 3 - heading
        elif map[r][c] == '+':
            if turn == 0:
                heading = (heading - 1) % 4
            elif turn == 2:
                heading = (heading + 1) % 4
            turn = (turn + 1) % 3

        if (r, c) in pos_occupied:
            print("Part 1:", "(" + str(c) + ", " + str(r) + ")")
            exit()
        new_carts.append((r, c, heading, turn))
        pos_occupied.add((r, c))
    carts = sorted(new_carts, key=lambda c: (c[0], c[1]))
    print(carts)
