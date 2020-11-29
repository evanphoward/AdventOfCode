lines = open("input").readlines()
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        l1, l2 = lines[i], lines[j]
        diff = 0
        for k in range(len(l1)):
            if l1[k] != l2[k]:
                diff += 1
            if diff > 1:
                break
        if diff == 1:
            line = ""
            for k in range(len(l1)):
                if l1[k] == l2[k]:
                    line += l1[k]
            print(line)
            exit(0)
