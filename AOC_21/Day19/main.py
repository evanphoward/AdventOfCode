from collections import Counter
inp = [scanner.split("\n")[1:] for scanner in open("input").read().split("\n\n")]
scanners = [[tuple(map(int, coord.split(","))) for coord in scanner] for scanner in inp]


def same_beacons(coords_1, coords_2):
    offset = []
    updated_coords = [[] for _ in range(len(coords_2))]
    for dim in range(3):
        dim_1 = [coord[dim] for coord in coords_1]
        for flip in (-1, 1):
            for matching_dim in range(3):
                dim_2 = [flip * coord[matching_dim] for coord in coords_2]
                matches = Counter([coord_2 - coord_1 for coord_2 in dim_2 for coord_1 in dim_1]).most_common(1)[0]
                if matches[1] >= 12:
                    offset.append(matches[0])
                    for i in range(len(updated_coords)):
                        updated_coords[i].append(dim_2[i] - offset[dim])
        if not offset:
            return False
    return [tuple(coord) for coord in updated_coords], tuple(offset)


beacons = set()
scanner_coords = set()
q = [scanners[0]]
rest = scanners[1:]
while q:
    aligned = q.pop()
    next_rest = []
    for candidate in rest:
        b = same_beacons(aligned, candidate)
        if b:
            q.append(b[0])
            scanner_coords.add(b[1])
        else:
            next_rest.append(candidate)
    rest = next_rest
    beacons.update(aligned)

print("Part 1:", len(beacons))
print("Part 2:", max(sum(abs(scanner_1[i] - scanner_2[i]) for i in range(3))
                     for scanner_2 in scanner_coords
                     for scanner_1 in scanner_coords))
