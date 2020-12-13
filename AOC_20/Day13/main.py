from functools import reduce

# Following functions from Rosetta Code. Implementation of Chinese remainder theorem
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_time(start_time, ids):
    i = start_time
    while True:
        for id in ids:
            if i % id == 0:
                return (i - start_time) * id
        i += 1


lines = open("input").readlines()
print("Part 1:", get_time(int(lines[0]), set([int(id) for id in lines[1].split(",") if id != "x"])))

ids = lines[1].split(",")
print("Part 2:", chinese_remainder([int(id) for id in ids if id != "x"], [-i % int(ids[i]) for i in range(len(ids)) if ids[i] != "x"]))
