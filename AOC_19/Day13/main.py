from AOC_19.IntComputer import IntProcess


def update_screen(pixels, screen=dict()):
    for i in range(0, len(pixels), 3):
        screen[(pixels[i], pixels[i + 1])] = pixels[i + 2]
    return screen


def display(screen):
    for y in range(max([pixel[1] for pixel in screen.keys()]) + 1):
        row = ""
        for x in range(max([pixel[0] for pixel in screen.keys()]) + 1):
            row = row + str(screen[(x, y)])
        print(row)
    print("Score:", screen[(-1, 0)])


def loc(obj, screen):
    for y in range(max([pixel[1] for pixel in screen.keys()]) + 1):
        for x in range(max([pixel[0] for pixel in screen.keys()]) + 1):
            if screen[(x, y)] == obj:
                return x, y


screen = update_screen(IntProcess(open("input")).run())

print("Part 1:", sum([pixel == 2 for pixel in screen.values()]))

game = IntProcess(open("input"))
game.prog[0] = 2
while game.ip != -1 and sum([pixel == 2 for pixel in screen.values()]) > 0:
    b_x, b_y = loc(4, screen)
    p_x, _ = loc(3, screen)
    if p_x < b_x:
        inp = 1
    elif p_x > b_x:
        inp = -1
    else:
        inp = 0
    screen = update_screen(game.run([inp]), screen)
    # display(screen)

print("Part 2:")
display(screen)



