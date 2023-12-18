import heapq

def dist(pos_a, pos_b):
    return sum(abs(pos_a[i] - (pos_b[i])) for i in range(3))

def intersects(box, bot):
    distance = 0
    for i in range(3):
        box_low, box_high = box[0][i], box[1][i] - 1
        distance += abs(bot[1][i] - box_low) + abs(bot[1][i] - box_high)
        distance -= box_high - box_low
    distance //= 2
    return distance <= bot[0]


inp = open("input").read().split("\n")
bots = []
for bot in inp:
    pos, r = bot.split(", ")
    pos = tuple(map(int, pos[5:-1].split(",")))
    r = int(r[2:])
    bots.append((r, pos))

best_bot = sorted(bots, reverse=True)[0]
print("Part 1:", sum(dist(best_bot[1], bot[1]) <= best_bot[0] for bot in bots))


initial_box = ((-100000000, -100000000, -100000000), (100000000, 100000000, 100000000))
q = [(-len(bots), -200000000, 300000000, initial_box)]
while q:
    neg_num_bots, neg_size, dist_to_orig, box = heapq.heappop(q)
    if neg_size == -1:
        print("Part 2:", dist_to_orig)
        break
    new_size = neg_size // -2
    for octant in [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
                   (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]:
        new_box_0 = tuple(box[0][i] + new_size * octant[i] for i in (0, 1, 2))
        new_box_1 = tuple(new_box_0[i] + new_size for i in (0, 1, 2))
        new_box = (new_box_0, new_box_1)
        new_num_bots = sum(intersects(new_box, bot) for bot in bots)
        heapq.heappush(q,(-new_num_bots, -new_size, dist(new_box_0, (0, 0, 0)), new_box))