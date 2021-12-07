gift = {"children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}
aunts = []
for aunt in open("input").readlines():
    aunt = aunt.replace(",", "").replace(":", "").strip().split()
    aunts.append({aunt[2]: int(aunt[3]), aunt[4]: int(aunt[5]), aunt[6]: int(aunt[7])})

for i, aunt in enumerate(aunts):
    for attr in gift:
        if attr in aunt:
            if gift[attr] != aunt[attr]:
                break
        else:
            continue
    else:
        print("Part 1:", i + 1)

for i, aunt in enumerate(aunts):
    for attr in gift:
        if attr in aunt:
            if attr in ["cats", "trees"]:
                if aunt[attr] <= gift[attr]:
                    break
            elif attr in ["pomeranians", "goldfish"]:
                if aunt[attr] >= gift[attr]:
                    break
            elif gift[attr] != aunt[attr]:
                break
        else:
            continue
    else:
        print("Part 2:", i + 1)
