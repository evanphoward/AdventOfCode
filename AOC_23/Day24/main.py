from MiscFiles.library import *

inp = get_input(2023, 24).split("\n")
points = []
for line in inp:
    pos, vel = line.split(" @ ")
    points.append((tuple(map(int, pos.split(", "))), tuple(map(int, vel.split(", ")))))

ans = 0
for i, p1 in enumerate(points):
    for p2 in points[i + 1:]:
        try:
            intersect = np.linalg.solve([[p1[1][0], -p2[1][0]], [p1[1][1], -p2[1][1]]], [p2[0][0] - p1[0][0], p2[0][1] - p1[0][1]])
        except np.linalg.LinAlgError:
            continue
        if intersect[0] > 0 and intersect[1] > 0:
            x = p1[0][0] + p1[1][0] * intersect[0]
            y = p1[0][1] + p1[1][1] * intersect[0]
            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                ans += 1

print("Part 1:", ans)

solver = z3.Solver()
I = lambda name: z3.BitVec(name, 64)
x, y, z = I('x'), I('y'), I('z')
vx, vy, vz = I('vx'), I('vy'), I('vz')

# Very over-specified system, only need first four points to get correct solution
for i, ((px, py, pz), (vax, vay, vaz)) in enumerate(points[:4]):
    t = I(f't_{i}')
    solver.add(t >= 0)
    solver.add(x + vx * t == px + vax * t)
    solver.add(y + vy * t == py + vay * t)
    solver.add(z + vz * t == pz + vaz * t)

assert solver.check() == z3.sat
m = solver.model()
print("Part 2:", sum(m.eval(val).as_long() for val in (x, y, z)))

