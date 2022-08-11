numRecipes = int(open("input").read())
numRecipesList = [int(x) for x in str(numRecipes)]

def progressRecipes(validRecipesIndex, newRecipe):
    if numRecipesList[validRecipesIndex] == newRecipe:
            validRecipesIndex += 1
            if validRecipesIndex == len(numRecipesList):
                print("Part 2:", len(recipes) - len(numRecipesList))
                exit()
            return validRecipesIndex
    else:
        return 0

recipes = [3, 7]
elf1 = 0
elf2 = 1
validRecipesIndex = 0

while True:
    newRecipe = recipes[elf1] + recipes[elf2]

    if newRecipe >= 10:
        recipes.append(1)
        validRecipesIndex = progressRecipes(validRecipesIndex, 1)
        newRecipe -= 10

    recipes.append(newRecipe)
    validRecipesIndex = progressRecipes(validRecipesIndex, newRecipe)

    if len(recipes) == numRecipes + 10:
        print("Part 1:", ''.join(str(x) for x in recipes[numRecipes:(numRecipes + 10)]))

    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

