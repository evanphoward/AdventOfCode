from MiscFiles.library import *

def check(nums, remove):
    if remove != -1:
        nums = nums[:remove] + nums[remove+1:]
    if not (nums == sorted(nums) or nums == sorted(nums)[::-1]):
        return False
    good = True
    for i in range(len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) > 3 or nums[i] == nums[i + 1]:
            good = False
    return good

inp = get_input(2024, 2).split("\n")
p1, p2 = 0, 0
for line in inp:
    nums = [int(x) for x in line.split()]
    safes = [check(nums, i) for i in range(-1, len(nums))]
    p1 += safes[0]
    p2 += any(safes)

print("Part 1:", p1)
print("Part 2:", p2)
