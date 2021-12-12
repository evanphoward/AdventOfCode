# Get a list of all possible subsets of weights ending at index n that add up to goal
def get_total_subset_sums(weights, n, goal):
    if goal == 0:
        return [[]]
    if n == 0:
        return -1

    if weights[n - 1] > goal:
        return get_total_subset_sums(weights, n - 1, goal)

    include_last_sum = get_total_subset_sums(weights, n - 1, goal - weights[n - 1])
    exclude_last_sum = get_total_subset_sums(weights, n - 1, goal)
    if include_last_sum == -1:
        return exclude_last_sum
    if exclude_last_sum == -1:
        return [subset + [weights[n - 1]] for subset in include_last_sum]
    return [subset + [weights[n - 1]] for subset in include_last_sum] + exclude_last_sum


# Find the minimum quantum entanglement of the smallest subset
def min_qe(subsets):
    ideal_length = min(len(x) for x in subsets)
    qes = []
    for subset in list(filter(lambda x: len(x) == ideal_length, subsets)):
        ans = 1
        for weight in subset:
            ans *= weight
        qes.append(ans)
    return min(qes)


total_weights = list(map(int, open("input").readlines()))
print("Part 1:", min_qe(get_total_subset_sums(total_weights, len(total_weights), sum(total_weights) // 3)))
print("Part 2:", min_qe(get_total_subset_sums(total_weights, len(total_weights), sum(total_weights) // 4)))
