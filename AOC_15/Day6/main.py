pts = dict()
pts_2 = dict()

TOGGLE = 0
TURN_ON = 1
TURN_OFF = 2


def operate(pt_1, pt_2, op):
    global pts
    global pts_2
    for x in range(pt_1[0], pt_2[0] + 1):
        for y in range(pt_1[1], pt_2[1] + 1):
            if op == TOGGLE:
                pts[(x, y)] = 1 if pts[(x, y)] == 0 else 0
                pts_2[(x, y)] += 2
            elif op == TURN_ON:
                pts[(x, y)] = 1
                pts_2[(x, y)] += 1
            elif op == TURN_OFF:
                pts[(x, y)] = 0
                if pts_2[(x, y)] > 0:
                    pts_2[(x, y)] -= 1


for x in range(0, 1000):
    for y in range(0, 1000):
        pts[(x, y)] = 0
        pts_2[(x, y)] = 0

for instruc in open("input"):
    oper = -1
    point_offset = 0
    instruc = instruc.split(" ")
    if instruc[0] == "turn":
        point_offset = 1
        if instruc[1] == "on":
            oper = TURN_ON
        if instruc[1] == "off":
            oper = TURN_OFF
    else:
        oper = TOGGLE

    first_point = instruc[1+point_offset].split(",")
    first_point = (int(first_point[0]), int(first_point[1]))

    second_point = instruc[3 + point_offset].split(",")
    second_point = (int(second_point[0]), int(second_point[1]))

    operate(first_point, second_point, oper)

print("Part 1:", sum(pts.values()))
print("Part 2:", sum(pts_2.values()))

