from AOC_19.IntComputer import IntProcess


def display(image, view):
    print(''.join([chr(x) for x in image]))
    x = y = 0
    for i in image:
        if chr(i) == "\n":
            x = 0
            y += 1
            continue
        view[(x, y)] = chr(i)
        x += 1
    return view


camera = IntProcess(open("input"))
view = display(camera.run(), dict())
total = 0
for x in range(1, 38):
    for y in range(1, 42):
        if all([view[(x, y)] == '#', view[(x + 1, y)] == '#', view[(x - 1, y)] == '#', view[(x, y + 1)] == '#', view[(x, y - 1)] == '#']):
            total += x * y
print("Part 1:", total)

# Did this part by hand :-/. This is from a text document I used for notes.
# R,4,L,10,L,10,L,8,R,12,R,10,R,4,R,4,L,10,L,10,L,8,R,12,R,10,R,4,R,4,L,10,L,10,L,8,L,8,R,10,R,4,L,8,R,12,R,10,R,4,L,8,L,8,R,10,R,4,R,4,L,10,L,10,L,8,L,8,R,10,R,4
# A = R4
# B = L10
# C = L8
# D = R12
# E = R10
# ABB CDEA ABB CDEA ABB CCEA CDEA CCEA ABB CCEA
# A = ABB = R,4,L,10,L,10
# B = CDEA = L,8,R,12,R,10,R,4
# C = CCEA = L,8,L,8,R,10,R,4
# A,B,A,B,A,C,B,C,A,C

camera = IntProcess(open("input"))
camera.prog[0] = 2
inp = "A,B,A,B,A,C,B,C,A,C\nR,4,L,10,L,10\nL,8,R,12,R,10,R,4\nL,8,L,8,R,10,R,4\nn\n"
inp = [ord(x) for x in inp]
out = camera.run(inp)
print("Part 2:", out[len(out) - 1])
