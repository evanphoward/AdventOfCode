def compare_carts(cart1, cart2):
    cart1_r, cart1_c, _ = cart1
    cart2_r, cart2_c, _ = cart2

    if cart1_r < cart2_r:
        return -1
    elif cart1_r > cart2_r:
        return 1
    else:
        if cart1_c < cart2_c:
            return -1
        elif cart1_c > cart2_c:
            return 1
        else:
            return 0

map = open("input").read().split("\n")
WIDTH = len(map[0])
HEIGHT = len(map)
carts = []
for r in range(HEIGHT):
    for c in range(WIDTH):
        if map[r][c] == '^':
            carts.append((r, c, 0))
        elif map[r][c] == '>':
            carts.append((r, c, 1))
        elif map[r][c] == 'v':
            carts.append((r, c, 2))
        elif map[r][c] == '<':
            carts.append((r, c, 3))

correct_mapping = {'|': '|', '-': '-', '/': '/', '\\': '\\', '^': '|', 'v': '|', '<': '-', '>': '-', ' ': ' ', '+': '+'}
map = [[correct_mapping[cell] for cell in line] for line in map]

while True:
    new_carts = []
    pos_occupied = set()
    for r, c, heading in carts:
        if c < 0:
            print(r, c, heading)
        # print(r, c, heading)
        if heading == 0:
            r -= 1
            if map[r][c] == '/':
                heading = 1
        elif heading == 1:
            c += 1
            if map[r][c] == '\\':
                heading = 2
        elif heading == 2:
            r += 1
            if map[r][c] == '/':
                heading = 3
        elif heading == 3:
            c -= 1
            if map[r][c] == '\\':
                heading = 0
        if (r, c) in pos_occupied:
            print("Part 1:", "(" + r + ", " + c + ")")
            exit()
        new_carts.append((r, c, heading))
        pos_occupied.add((r, c))
    carts = sorted(new_carts, cmp=compare_carts)
