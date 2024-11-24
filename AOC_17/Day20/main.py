from MiscFiles.library import *

class Particle:
    def __init__(self, id, line):
        self.id = id
        p, v, a = [list(map(int, x[x.index('<') + 1:x.index('>')].split(','))) for x in line.split(", ")]
        self.position = p
        self.velocity = v
        self.acceleration = a

    def update(self):
        self.velocity = [x + y for x, y in zip(self.velocity, self.acceleration)]
        self.position = [x + y for x, y in zip(self.position, self.velocity)]

    def dist(self):
        return sum(abs(x) for x in self.position)


def simulate(remove):
    inp = get_input(2017, 20).split("\n")
    particles = []
    for i, line in enumerate(inp):
        particles.append(Particle(i, line))
    for _ in range(1000):
        for particle in particles:
            particle.update()
        if remove:
            positions = Counter([tuple(p.position) for p in particles])
            particles = [particle for particle in particles if positions[tuple(particle.position)] == 1]
    if remove:
        return len(particles)
    return sorted(particles, key=lambda particle: particle.dist())[0].id


print("Part 1:", simulate(remove=False))
print("Part 2:", simulate(remove=True))