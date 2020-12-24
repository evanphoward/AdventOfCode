def solve(p2):
    initial = "247819356"

    N = int(1e6) if p2 else 9
    cups = [-1]*(int(1e6) + 1 if p2 else len(initial) + 1)
    for i in range(len(initial) - 1):
        cups[int(initial[i])] = int(initial[(i + 1)])

    cups[int(initial[-1])] = 10 if p2 else int(initial[0])
    if p2:
        for i in range(len(initial) + 1, int(1e6)):
            cups[i] = i + 1
        cups[int(1e6)] = int(initial[0])

    current = int(initial[0])
    for _ in range(int(1e7) if p2 else 100):
        moved_cups = list()
        tmp = cups[current]
        for _ in range(3):
            moved_cups.append(tmp)
            tmp = cups[tmp]

        cups[current] = tmp
        dest = N if current == 1 else current - 1
        while dest in moved_cups:
            dest = N if dest == 1 else dest - 1

        tmp = cups[dest]
        for i in range(3):
            cups[dest] = moved_cups[i]
            dest = moved_cups[i]
        cups[dest] = tmp

        current = cups[current]

    if p2:
        return cups[1] * cups[cups[1]]
    else:
        tmp = cups[1]
        string = ""
        while tmp != 1:
            string = string + str(tmp)
            tmp = cups[tmp]
        return string


print(solve(False))
print(solve(True))
