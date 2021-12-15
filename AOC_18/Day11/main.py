import numpy
serial_number = int(open("input").read())


def power(x, y):
    return ((((((x + 10) * y) + serial_number) * (x + 10)) // 100) % 10) - 5


p_levels = numpy.fromfunction(power, (300, 300))
best_power = bx = by = bs = 0
for size in range(3, 300):
    square_power_levels = sum(p_levels[x:x-size+1 or None, y:y-size+1 or None] for x in range(size) for y in range(size))
    max_power = square_power_levels.max()
    if max_power < 0:
        break
    coord = numpy.where(square_power_levels == max_power)
    if max_power > best_power:
        best_power = max_power
        bx = coord[0][0]
        by = coord[1][0]
        bs = size
    if size == 3:
        print("Part 1:", f"{coord[0][0]},{coord[1][0]}")

print("Part 2:", f"{bx},{by},{bs}")
