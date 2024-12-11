from MiscFiles.library import *

inp = list(map(int, get_input(2024, 11).split()))

def step(stones):
    new_stones = defaultdict(int)
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[stone]
        elif len(str(stone)) % 2 == 0:
            left = int(str(stone)[:len(str(stone))//2])
            right = int(str(stone)[len(str(stone))//2:])
            new_stones[left] += stones[stone]
            new_stones[right] += stones[stone]
        else:
            new_stones[stone * 2024] += stones[stone]
    return new_stones


stones = Counter(inp)
for i in range(25):
    stones = step(stones)
print("Part 1:", sum(stones.values()))

stones= Counter(inp)
for _ in range(75):
    stones = step(stones)
print("Part 2:", sum(stones.values()))
