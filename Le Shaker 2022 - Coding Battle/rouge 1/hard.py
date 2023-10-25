import sys, io

sampleToTest = "1"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START
def maxRecipe(recipe, listTotalBerry):
    RB1, RB2, RB3, NRJ = recipe
    TB1, TB2, TB3 = listTotalBerry
    result = 0
    if RB1 != 0:
        result = TB1 // RB1
    if RB2 != 0:
        result = max(result, TB2 // RB2)
    if RB3 != 0:
        result = max(result, TB3 // RB3)
    return result


class counter:
    def __init__(self, listAllRecipe):
        self.counter = self.buildCounter(listAllRecipe)

    def buildCounter(self, listAllRecipe):
        counter = []
        for recipe in listAllRecipe:
            counter.append([0, recipe[4]])
        return counter

    @staticmethod
    def listWithIntToHex(listeRecipeIndex):
        if listeRecipeIndex[0] > 15:
            print("-------------c'est la merde--------------")
            print("------------oublie la base 16------------")
        return format(listeRecipeIndex[0], "x")

    def counterToString(self):
        return "".join(map(self.listWithIntToHex, self.counter))

    def isEmptyCounter(self):
        return self.counterToString() == "0" * len(self.counter)

    def plus1ToCounter(self):
        for recipeIndex in self.counter:
            recipeIndex[0] += 1
            if not recipeIndex[0] > recipeIndex[1]:
                return True
            recipeIndex[0] = 0
        return False


    # TODO c'est tres sus comme technique faire gaffe aux reset pas et qui fait des boucles infinies
    def getToPreviousRecipe(self):
        for index, recipeCounter in enumerate(self.counter[::-1]):
            if recipeCounter[0]:
                recipeCounter[0] = 0
                self.plus1ToCounter()
                break


result = ""
print(result)

listTotalBerry = tuple(map(int, input().split()))
intNumberOfRecipe = int(input())

listAllRecipe = []
# TODO condition d'arret
run = True
for _ in range(intNumberOfRecipe):
    recipe = list(map(int, input().split()))
    recipe.append(maxRecipe(recipe, listTotalBerry))
    listAllRecipe.append(recipe)

# TODO remove this shit
print(listAllRecipe)

counter = counter(listAllRecipe)

print("1_______________________")
print(counter.counterToString())
counter.plus1ToCounter()
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
# plus1ToCounter(counter)
print("2_______________________")
print(counter.counterToString())

# print(counterToString(counter))
print("3_______________________")
# getToPreviousRecipe(counter)
print(counter.counter)

# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide → output = <|{result}|> contre exepct = <|{outputExpected}|>")
