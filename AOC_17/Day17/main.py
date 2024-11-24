from MiscFiles.library import *

steps = int(get_input(2017, 17))

buffer = deque([0])
for i in range(1, 2018):
    buffer.rotate(-steps)
    buffer.append(i)
print("Part 1:", buffer[0])

pos = 0
ans = 0
for i in range(1, 50000000 + 1):
    pos = ((pos + steps) % i) + 1
    if pos == 1:
        ans = i
print("Part 2:", ans)
