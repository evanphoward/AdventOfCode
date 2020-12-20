import re
import math


# Returns the given side of a tile as a string
def get_side(t, side, flipped=False):
    if side == 0:
        return ''.join([t[(0, c)] for c in (range(10) if not flipped else reversed(range(10)))])
    if side == 1:
        return ''.join([t[(r, 9)] for r in (range(10) if not flipped else reversed(range(10)))])
    if side == 2:
        return ''.join([t[(9, c)] for c in (range(10) if not flipped else reversed(range(10)))])
    if side == 3:
        return ''.join([t[(r, 0)] for r in (range(10) if not flipped else reversed(range(10)))])


# Returns a list either empty or with a tuple matching the sides of two tiles
def match_side(num1, num2):
    t1 = tiles[num1]
    t2 = tiles[num2]
    matches = list()
    for i in range(4):
        for j in range(4):
            if get_side(t1, i) == get_side(t2, j):
                matches.append((i, j, False))
            if get_side(t1, i, True) == get_side(t2, j):
                matches.append((i, j, True))
    return matches


# Flips a tile either vertically or horizontally
def flip(tile, vert):
    new_tile = dict()
    width = max(num[0] for num in tile) + 1
    for r in range(width):
        for c in range(width):
            new_tile[(r, c)] = tile[(width - r - 1, c)] if vert else tile[(r, width - c - 1)]
    return new_tile


# Rotates a tile either left or right
def rotate(tile, right):
    new_tile = dict()
    width = max(num[0] for num in tile) + 1
    for r in range(width):
        for c in range(width):
            new_tile[(r, c)] = tile[(width - c - 1, r)] if right else tile[(c, width - r - 1)]
    return new_tile


# Takes a tile and moves it so side is on the side denoted by dir
def orient(tile, side, dir, to_flip):
    global tiles
    if side == dir and not to_flip:
        return tile
    if to_flip:
        tile = flip(tile, side in [1, 3])
    if abs(dir - side) == 2:
        tile = flip(tile, side in [0, 2])
    if dir - side == 1:
        tile = rotate(tile, True)
    if dir - side == -1:
        tile = rotate(tile, False)
    return tile


# Fills in the edges of an image, done denotes how many layers have been done
def getedges(done):
    global prev_tile
    global edges
    for i in range(done + 1, length - done):
        for tile, map in tiles.items():
            if tile not in image.values() and tile in edges and len(match_side(prev_tile, tile)) == 1:
                if done == 0 or len(match_side(image[done - 1, i], tile)) == 1:
                    image[(done, i)] = tile
                    prev_tile = tile
                    break
    prev_tile = image[(done, done)]
    for i in range(done + 1, length - done):
        for tile, map in tiles.items():
            if tile not in image.values() and tile in edges and len(match_side(prev_tile, tile)) == 1:
                if done == 0 or len(match_side(image[i, done - 1], tile)) == 1:
                    image[(i, done)] = tile
                    prev_tile = tile
                    break
    prev_tile = image[(length - done - 1, done)]
    for i in range(done + 1, length - done):
        for tile, map in tiles.items():
            if tile not in image.values() and tile in edges and len(match_side(prev_tile, tile)) == 1:
                if done == 0 or len(match_side(image[length - done, i], tile)) == 1:
                    image[(length - done - 1, i)] = tile
                    prev_tile = tile
                    break
    prev_tile = image[(done, length - done - 1)]
    for i in range(done + 1, length - done - 1):
        for tile, map in tiles.items():
            if tile not in image.values() and tile in edges and len(match_side(prev_tile, tile)) == 1:
                if done == 0 or len(match_side(image[i, length - done], tile)) == 1:
                    image[(i, length - done - 1)] = tile
                    prev_tile = tile
                    break
    new_edges = set()
    for tile in tiles:
        if tile not in edges:
            edge_match = sum(len(match_side(tile, t2)) for t2 in tiles if (tile != t2 and t2 not in edges))
            if edge_match < 4:
                new_edges.add(tile)
            if len(match_side(tile, image[(done + 1, done)])) == 1 and len(match_side(tile, image[(done, done + 1)])) == 1:
                image[(done + 1, done + 1)] = tile
                prev_tile = tile
    edges = edges.union(new_edges)


# Format the tiles
tiles_s = list([l.strip() for l in open("input").read().split("\n\n")])
tiles = dict()
for tile in tiles_s:
    tile = tile.split("\n")
    tile_num = int(re.findall(r'\d+', tile[0])[0])
    tile = tile[1:]
    tile_map = dict()
    for r, row in enumerate(tile):
        for c, ch in enumerate(row):
            tile_map[(r, c)] = ch
    tiles[tile_num] = tile_map

# Find all the edges and multiply the ids of the corners
p = 1
prev_tile = None
edges = set()
for tile in tiles:
    edges_match = sum(len(match_side(tile, t2)) for t2 in tiles if tile != t2)
    if edges_match < 4:
        edges.add(tile)
    if edges_match == 2:
        p *= tile
        if prev_tile is None:
            prev_tile = tile
print("Part 1:", p)
image = {(0, 0): prev_tile}
length = int(math.sqrt(len(tiles)))

# Fill in the whole image
for i in range(math.floor(length / 2)):
    getedges(i)

# Orient all tiles correctly vertically
for r in range(length - 1):
    for c in range(length):
        down = match_side(image[(r, c)], image[(r + 1, c)])[0]
        tiles[image[(r, c)]] = orient(tiles[image[(r, c)]], down[0], 2, down[2])
        tiles[image[(r + 1, c)]] = orient(tiles[image[(r + 1, c)]], down[1], 0, False)

# Orient all tiles correctly horizontally
for r in range(length):
    for c in range(length - 1):
        right = match_side(image[(r, c)], image[(r, c + 1)])[0]
        tiles[image[(r, c)]] = orient(tiles[image[(r, c)]], right[0], 1, right[2])
        tiles[image[(r, c + 1)]] = orient(tiles[image[(r, c + 1)]], right[1], 3, False)

# Remove the borders from the iamge
real_image = dict()
r2 = 0
c2 = 0
for r in range(length * 10):
    if r % 10 in [0, 9]:
        continue
    for c in range(length * 10):
        if c % 10 in [0, 9]:
            continue
        real_image[(r2, c2)] = tiles[image[(r // 10, c // 10)]][(r % 10, c % 10)]
        c2 += 1
    c2 = 0
    r2 += 1
image = real_image
length *= 8

# Try all possible orientations and get the number of monsters by a regex
# If there are monsters, get the number of # not part of a monster
for i in range(4):
    for j in range(4):
        for b in [True, False]:
            rot_image = orient(image, i, j, b)
            regexable_image = ''.join([''.join([rot_image[r, c] for c in range(length)]) for r in range(length)])
            monsters = re.findall('(?=#.{'+str(length - 19)+'}#....##....##....###.{'+str(length - 19)+'}#..#..#..#..#..#)', regexable_image)
            if len(monsters) > 0:
                print("Part 2:", regexable_image.count("#") - len(monsters) * 15)
                exit()
