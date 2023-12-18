import numpy as np
MAPPINGS = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
def run(p1):
    boundary = 0
    rs = []
    cs = []
    r, c = 0, 0
    for line in open("input").read().split("\n"):
        line = line.split()

        if p1:
            dr, dc = MAPPINGS[line[0]]
            dist = int(line[1])
        else:
            dr, dc = list(MAPPINGS.values())[int(line[2][-2])]
            dist = int(line[2][2:-2], 16)
        r += (dr * dist)
        c += (dc * dist)
        rs.append(r)
        cs.append(c)
        boundary += dist

    def shoelace(x, y):
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


    area = shoelace(np.array(rs, dtype='int64'), np.array(cs, dtype='int64'))
    interior = (area + 1) - (boundary / 2)
    return interior + boundary


print("Part 1:", int(run(True)))
print("Part 2:", int(run(False)))

