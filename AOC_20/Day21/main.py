allergens_pos = dict()
ingredient_count = dict()
for line in open("input").readlines():
    l = line[:-2].strip().split(" (contains ")
    ingredients = l[0].split()
    for ingredient in ingredients:
        if ingredient not in ingredient_count:
            ingredient_count[ingredient] = 0
        ingredient_count[ingredient] += 1

    for allergen in l[1].split(", "):
        if allergen not in allergens_pos:
            allergens_pos[allergen] = set(ingredients)
        else:
            allergens_pos[allergen] = allergens_pos[allergen] & set(ingredients)

print("Part 1:", sum(ingredient_count[ingredient] for ingredient in ingredient_count if all(ingredient not in pos for pos in allergens_pos.values())))

while any(len(pos) > 1 for pos in allergens_pos.values()):
    for allergen, pos in allergens_pos.items():
        if len(pos) == 1:
            value = list(pos)[0]
            for allergen1 in allergens_pos:
                if allergen != allergen1 and value in allergens_pos[allergen1]:
                    allergens_pos[allergen1].remove(value)

print("Part 2:", ','.join([list(allergens_pos[a])[0] for a in sorted(list(allergens_pos.keys()))]))