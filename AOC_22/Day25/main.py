def decode_num(num):
    ans = []
    add = False
    while num > 0:
        remainder = num % 5 + add
        num //= 5
        add = remainder in (3, 4, 5)
        ans.append({0: "0", 1: "1", 2: "2", 3: "=", 4: "-", 5: "0"}[remainder])
    return ans


inp = open("input").read().strip().split("\n")
mapping = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
total = sum(sum((5 ** i) * mapping[x[len(x) - 1 - i]] for i in range(len(x))) for x in inp)
print("Part 1:", ''.join(decode_num(total)[::-1]))
