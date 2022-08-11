class Unit:
    def __init__(self, x, y, elf):
        self.x = x
        self.y = y
        self.elf = elf
        self.hp = 200
        self.attack = 3

    def __repr__(self):
        return ("E" if self.elf else "G") + "(" + str(self.hp) + ") @ " + str(self.x) + "," + str(self.y)

    def move():
        global MAP, UNITS
        pass

MAP = dict()
UNITS = []
for y, line in enumerate(open("input").read().split("\n")):
    for x, cell in enumerate(line):
        if cell in "GE":
            UNITS.append(Unit(x, y, cell == "E"))
            cell = "."
        MAP[(x, y)] = cell