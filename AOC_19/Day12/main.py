import math


class Moon:
    def __init__(self, moon):
        self.pos = [int(moon[0][3:]), int(moon[1][2:]), int(moon[2][2:-1])]
        self.vel = [0, 0, 0]
        self.start = [(self.pos[i], self.vel[i]) for i in range(3)]
        self.step = 0

    def update_vel(self, moon_2):
        for i in range(3):
            if self.pos[i] < moon_2.pos[i]:
                self.vel[i] += 1
            elif self.pos[i] > moon_2.pos[i]:
                self.vel[i] -= 1

    def update_pos(self):
        self.step += 1
        for i in range(3):
            self.pos[i] += self.vel[i]


moons = []
for line in open("input").readlines():
    moons.append(Moon(line.strip().split(", ")))

lcms = dict()
while len(lcms) < 3:
    for m_1 in moons:
        for m_2 in moons:
            if m_1 == m_2:
                continue
            m_1.update_vel(m_2)

    for m in moons:
        m.update_pos()

    if moons[0].step == 1000:
        print("Part 1:", sum(sum([abs(z) for z in moons[i].vel]) * sum([abs(z) for z in moons[i].pos]) for i in range(4)))

    for i in range(3):
        if all(moons[j].pos[i] == moons[j].start[i][0] for j in range(4)) and \
                all(moons[j].vel[i] == moons[j].start[i][1] for j in range(4)) and \
                i not in lcms:
            lcms[i] = math.lcm(moons[0].step, moons[1].step, moons[2].step, moons[3].step)


lcms = [lcm for lcm in lcms.values()]
print("Part 2:", math.lcm(lcms[0], lcms[1], lcms[2]))
