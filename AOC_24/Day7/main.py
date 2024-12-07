from MiscFiles.library import *

inp = get_input(2024, 7).split("\n")

def total_calibration(num_operations):
    global inp
    total_ans = 0
    for line in inp:
        ans, nums = line.split(': ')
        ans = int(ans)
        nums = list(map(int, nums.split()))
        for values in itertools.product(list(range(num_operations)), repeat=(len(nums) - 1)):
            pos = nums[0]
            for i in range(1, len(nums)):
                if values[i - 1] == 0:
                    pos *= nums[i]
                elif values[i - 1] == 1:
                    pos += nums[i]
                else:
                    pos = int(str(pos) + str(nums[i]))
                if pos > ans:
                    break
            if pos == ans:
                total_ans += ans
                break
    return total_ans


print("Part 1:", total_calibration(2))
print("Part 2:", total_calibration(3))
