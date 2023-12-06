times = [int(x) for x in open("input").read().split("\n")[0].split()[1:]]
distances = [int(x) for x in open("input").read().split("\n")[1].split()[1:]]


def num_ways_to_win(time, record_distance):
    num_wins = 0
    for speed in range(time):
        distance = speed * (time - speed)
        if distance > record_distance:
            num_wins += 1
    return num_wins


ans = 1
for race in range(len(times)):
    ans *= num_ways_to_win(times[race], distances[race])

print("Part 1:", ans)
print("Part 2:", num_ways_to_win(int(''.join(map(str, times))), int(''.join(map(str, distances)))))