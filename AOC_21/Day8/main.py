import itertools

segs_to_nums = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4,
                "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}


total_1 = 0
total_2 = 0
total_segs = "abcdefg"
for line in open("input").readlines():
    input_nums, output_nums = line.strip().split(" | ")
    input_nums = input_nums.split()
    output_nums = output_nums.split()
    for num in output_nums:
        if len(num) in [2, 3, 4, 7]:
            total_1 += 1
    for perm in itertools.permutations(total_segs):
        segs_to_segs = dict()
        for i, seg in enumerate(perm):
            segs_to_segs[seg] = total_segs[i]
        inp = ["".join(segs_to_segs[seg] for seg in num) for num in input_nums]
        out = ["".join(segs_to_segs[seg] for seg in num) for num in output_nums]
        if all("".join(sorted(num)) in segs_to_nums for num in inp):
            out = ["".join(sorted(x)) for x in out]
            total_2 += int("".join(str(segs_to_nums[x]) for x in out))
            break


print("Part 1:", total_1)
print("Part 2:", total_2)