from collections import Counter
import difflib
print("Part 1:", sum(3 in Counter(line.strip()).values() for line in open("input").readlines()) *
                 sum(2 in Counter(line.strip()).values() for line in open("input").readlines()))
for line_a in open("input").read().split("\n"):
    for line_b in open("input").read().split("\n"):
        differences = list(difflib.ndiff(line_a, line_b))
        if len(differences) - len(line_a) == 1:
            print("Part 2:", ''.join(c[-1] for c in differences if '-' not in c and '+' not in c))
            exit()
