import math


class Reaction:
    def __init__(self, rxn):
        rxn = rxn.strip().split(" => ")
        inputs = rxn[0].split(", ")
        self.inputs = []
        for i in inputs:
            num, chem = i.split(" ")
            self.inputs.append((int(num), chem))
        output = rxn[1].split(" ")
        self.output = [int(output[0]), output[1]]

    def rev(self, amt):
        overflow = self.output[0] - (amt % self.output[0]) if amt % self.output[0] else 0
        amt = math.ceil(amt / self.output[0])
        return overflow, [(chem[0] * amt, chem[1]) for chem in self.inputs]

    def do_rxn(self, amt):
        global rxns, ingredients
        overflow, chems = self.rev(amt)
        for chem in chems:
            ingredients[chem[1]] -= chem[0]
        ingredients[self.output[1]] += amt + overflow


def do_all_rxns(chem, amt):
    global rxns, ingredients
    ingredients[chem] = -amt
    while any([val < 0 and key != "ORE" for key, val in ingredients.items()]):
        for k, v in ingredients.items():
            if k == "ORE":
                continue
            if v < 0:
                rxns[k].do_rxn(v * -1)


rxns = dict()
ingredients = {"ORE": 0}
for line in open("input").readlines():
    rxn = Reaction(line)
    ingredients[rxn.output[1]] = 0
    rxns[rxn.output[1]] = rxn

do_all_rxns("FUEL", 1)
print("Part 1:", ingredients["ORE"]*-1)

fuel = math.floor(1000000000000 / ingredients["ORE"] * -1)
for k in ingredients.keys():
    ingredients[k] = 0
ingredients["ORE"] = 1000000000000
do_all_rxns("FUEL", fuel)
delta = 10000
while ingredients["ORE"] > 0:
    do_all_rxns("FUEL", delta)
    fuel += delta
    delta = math.floor(((ingredients["ORE"] - 1000000) / (1000000000000 - 1000000)) * (10000 - 1) + 1
                       if ingredients["ORE"] > 1000000 else 1)
print("Part 2:", fuel - 1)



