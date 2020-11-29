freq = 0
lines = open("input").readlines()
seen_freq = set()
while True:
    for line in lines:
        line = line.strip()
        freq += int(line)
        if freq in seen_freq:
            print(freq)
            exit(0)
        seen_freq.add(freq)