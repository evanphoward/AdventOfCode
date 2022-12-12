inp = open("input").read().strip().split("\n")

files = {}
dirs = set()
path = []
for cmd in inp:
    if cmd.startswith("$ cd"):
        cmd = cmd.split()
        if cmd[2] == "..":
            if len(path) > 0:
                path = path[:-1]
        elif cmd[2] == "/":
            path = []
        else:
            path.append(cmd[2])
    elif not (cmd.startswith("dir") or cmd.startswith("$")):
        size, name = cmd.split()
        files['/'.join(path + [name])] = int(size)
    dirs.add('/'.join(path))

d_sizes = {}
for d in dirs:
    d_size = 0
    for file in files:
        if file.startswith(d):
            d_size += files[file]
    d_sizes[d] = d_size

print("Part 1:", sum(s for s in d_sizes.values() if s <= 100000))
print("Part 2:", sorted([d for d in d_sizes.values() if d >= d_sizes[''] - 40000000])[0])
