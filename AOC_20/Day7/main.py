class Bag:
    def __init__(self, line):
        words = line.strip().split(" ")
        self.color = (words[0], words[1])
        self.contains = []
        i = 4
        if words[i] != "no":
            while i < len(words) - 1:
                self.contains.append([int(words[i]), (words[i + 1], words[i + 2])])
                i += 4

    def shiny_gold(self):
        global bags
        if self.color == ("shiny", "gold"):
            return True
        if len(self.contains) == 0:
            return False
        return any([bags[sub_bag[1]].shiny_gold() for sub_bag in self.contains])

    def count(self):
        global bags
        if len(self.contains) == 0:
            return 1
        return 1 + sum([bags[sub_bag[1]].count() * sub_bag[0] for sub_bag in self.contains])


bags = dict()
for line in open("input").readlines():
    bag = Bag(line)
    bags[bag.color] = bag

print("Part 1:", sum([bag.shiny_gold() for bag in bags.values()]) - 1)
print("Part 2:", bags[("shiny", "gold")].count() - 1)