import functools


@functools.cache
def get_value(wire):
    global circuit
    if wire.isnumeric():
        return int(wire)
    values = circuit[wire].split()
    if len(values) == 1:
        return get_value(circuit[wire])
    if values[0] == "NOT":
        return ~get_value(values[1]) + 2**16
    if values[1] == "AND":
        return get_value(values[0]) & get_value(values[2])
    if values[1] == "OR":
        return get_value(values[0]) | get_value(values[2])
    if values[1] == "LSHIFT":
        return get_value(values[0]) << get_value(values[2])
    if values[1] == "RSHIFT":
        return get_value(values[0]) >> get_value(values[2])
    assert False


circuit = dict([reversed(line.strip().split(" -> ")) for line in open("input").readlines()])
circuit["b"] = str(get_value("a"))
get_value.cache_clear()
print("Part 1:", circuit["b"])
print("Part 2:", get_value("a"))

