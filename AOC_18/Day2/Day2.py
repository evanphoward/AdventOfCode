from collections import Counter
two, three = 0, 0
for line in open("input").readlines():
    counter = Counter(line.strip())
    tw, th = True, True
    for l in line:
        num = counter[l]
        if num == 2 and tw:
            two += 1
            tw = False
        if num == 3 and th:
            three += 1
            th = False

print(two * three)
