nums = [int(x.strip()) for x in open("input").readlines()]

invalid = 0
for i in range(25, len(nums)):
    curr_numbers = nums[i-25:i]
    if nums[i] not in set([n_1 + n_2 for n_1 in curr_numbers for n_2 in curr_numbers if n_1 != n_2]):
        invalid = nums[i]
        break
print("Part 1:", invalid)

for i in range(len(nums)):
    curr_sum = nums[i]
    j = i + 1
    while curr_sum < invalid:
        curr_sum += nums[j]
        j += 1
    if curr_sum == invalid and j != i + 1:
        print("Part 2:", min(nums[i:j]) + max(nums[i:j]))
        break
