from collections import defaultdict

class Cart:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.turn = 0
        self.active = True

map = defaultdict(lambda: "")
carts = []
for y, line in enumerate(open("input").read().split("\n")):
    for x, cell in enumerate(line):
        if cell in "^>v<":
            heading = {"^": 0, ">": 1, "v": 2, "<": 3}[cell]
            carts.append(Cart(x, y, heading))
            cell = {"^": "|", ">": "-", "v": "|", "<": "-"}[cell]
        if cell in "\\/+-":
            map[(x, y)] = cell

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
first_collision = False
while sum(c.active for c in carts) > 1:
    carts.sort(key=lambda c: (c.y, c.x))
    for ci, cart in enumerate(carts):
        if not cart.active:
            continue
        dx, dy = deltas[cart.heading]
        cart.x += dx
        cart.y += dy
        for c2i, cart2 in enumerate(carts):
            if c2i == ci:
                continue
            if cart.x == cart2.x and cart.y == cart2.y and cart2.active:
                cart.active = False
                cart2.active = False
                if not first_collision:
                    print("Part 1:", str(cart.x) + "," + str(cart.y))
                first_collision = True
                continue
        part = map[(cart.x, cart.y)]
        if (part == "/" and cart.heading in [0, 2]) or (part == "\\" and cart.heading in [1, 3]) or (part == "+" and cart.turn == 2):
            cart.heading = (cart.heading + 1) % 4
        elif (part == "/" and cart.heading in [1, 3]) or (part == "\\" and cart.heading in [0, 2]) or (part == "+" and cart.turn == 0):
            cart.heading = (cart.heading - 1) % 4
        if part == "+":
            cart.turn = (cart.turn + 1) % 3

for cart in carts:
    if cart.active:
        print("Part 2:", str(cart.x) + "," + str(cart.y))

