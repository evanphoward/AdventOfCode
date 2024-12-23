from MiscFiles.library import *

def mix(num_1, num_2):
    return num_1 ^ num_2

def prune(num):
    return num % 16777216

def get_secret(num):
    x = num * 64
    num = prune(mix(x, num))
    x = num // 32
    num = prune(mix(x, num))
    x = num * 2048
    num = prune(mix(x, num))
    return num


inp = get_input(2024, 22).split("\n")
scores = defaultdict(int)
two_thousandth = set()
for line in inp:
    changes = []
    num = int(line)
    seen = set()
    prev = num
    for _ in range(2000):
        num = get_secret(num)
        changes.append(num % 10 - prev)
        prev = num % 10
        to_add = tuple(changes[-4:])
        if len(changes) > 4 and to_add not in seen:
            seen.add(to_add)
            scores[to_add] += prev
    two_thousandth.add(num)


print("Part 1:", sum(two_thousandth))
print("Part 2:", max(scores.values()))
