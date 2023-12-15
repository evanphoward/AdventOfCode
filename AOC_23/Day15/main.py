def get_h(lbl):
    h = 0
    for ch in lbl:
        h = ((h + ord(ch)) * 17) % 256
    return h

inp = open("input").read().strip().split(",")
print("Part 1:", sum(get_h(x) for x in inp))

boxes = [dict() for _ in range(256)]
for x in inp:
    label = x[:-1] if x[-1] == "-" else x[:-2]
    box = get_h(label)
    if x[-1] == "-" and label in boxes[box]:
        boxes[box].pop(label)
    elif x[-2] == "=":
        boxes[box][label] = int(x[-1])

print("Part 2:", sum(sum((i + 1) * (j + 1) * fcl for j, fcl in enumerate(box.values())) for i, box in enumerate(boxes)))
