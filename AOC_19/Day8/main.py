WIDTH = 25
HEIGHT = 6

image = open("input").readline()
layers = []
x = y = 0
i = 0
for pixel in image:
    if x == 0 and y == 0:
        layers.append({})
    layers[i][(x, y)] = int(pixel)
    x += 1
    if x == WIDTH:
        x = 0
        y += 1
        if y == HEIGHT:
            y = 0
            i += 1


min_zeroes = 0
for i in range(1, len(layers)):
    if sum([x == 0 for x in layers[i].values()]) < sum([x == 0 for x in layers[min_zeroes].values()]):
        min_zeroes = i

print("Part 1:", sum([x == 1 for x in layers[min_zeroes].values()]) * sum([x == 2 for x in layers[min_zeroes].values()]))

image = {}
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        i = 0
        while layers[i][(x, y)] == 2:
            i += 1
        image[(x, y)] = layers[i][(x, y)]

print("Part 2:")
for y in range(0, HEIGHT):
    row = ""
    for x in range(0, WIDTH):
        row = row + str(image[x, y])
    print(row)
    # YLFPJ
