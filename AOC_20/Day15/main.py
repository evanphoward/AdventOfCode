nums = open("input").readline().split(",")
count = dict()
for i in range(len(nums) - 1):
    count[int(nums[i])] = (0, i + 1)
cur_num = int(nums[-1])
for i in range(len(nums) + 1, 30000001):
    if cur_num in count:
        count[cur_num] = (count[cur_num][1], i - 1)
        cur_num = count[cur_num][1] - count[cur_num][0]
    else:
        count[cur_num] = (0, i - 1)
        cur_num = 0
    if i == 2020:
        print("Part 1:", cur_num)
print("Part 2:", cur_num)
