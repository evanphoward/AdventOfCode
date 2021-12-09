print("Part 1:", sum(map(int, open("input").readlines())))
seen = set()
freq = 0
while True:
    for line in open("input").readlines():
        freq += int(line)
        if freq in seen:
            print("Part 2:", freq)
            exit()
        seen.add(freq)
