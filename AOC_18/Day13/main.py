from collections import defaultdict

class Cart:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading
        self.turn = 0

map = defaultdict(lambda: "")
carts = []
for y, line in enumerate(open("input").read().split("\n")):
    for x, cell in enumerate(line):
        if cell in "^>v<":
            heading = {"^": 0, ">": 1, "v": 2, "<": 3}[cell]
            carts.append(Cart(x, y, heading))
            part = {"^": "|", ">": "-", "v": "|", "<": "-"}[cell]
        else:
            part = cell
        if part in "\\/+-":
            map[(x, y)] = part

deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
while True:
    carts.sort(key=lambda c: (c.y, c.x))
    for ci, cart in enumerate(carts):
        dx, dy = deltas[cart.heading]
        cart.x += dx
        cart.y += dy
        if any(cart.x == cart2.x and cart.y == cart2.y for c2i, cart2 in enumerate(carts) if ci != c2i):
            print("Part 1:", str(cart.x) + "," + str(cart.y))
            exit()
        part = map[(cart.x, cart.y)]
        if (part == "/" and cart.heading in [0, 2]) or (part == "\\" and cart.heading in [1, 3]) or (part == "+" and cart.turn == 2):
            cart.heading = (cart.heading + 1) % 4
        elif (part == "/" and cart.heading in [1, 3]) or (part == "\\" and cart.heading in [0, 2]) or (part == "+" and cart.turn == 0):
            cart.heading = (cart.heading - 1) % 4
        if part == "+":
            cart.turn = (cart.turn + 1) % 3

