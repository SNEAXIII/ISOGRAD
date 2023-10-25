import sys, io

sampleToTest = "4"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START


class AllRecipe:
    def __init__(self):
        self.listAllRecipe = self.buildAllRecipe()
        self.allPossibilities = self.buildAllPossibilities()

    def buildAllRecipe(self):
        self.listTotalBerry = tuple(map(int, input().split()))
        intNumberOfRecipe = int(input())

        listAllRecipe = []
        for _ in range(intNumberOfRecipe):
            recipe = list(map(int, input().split()))
            recipe.append(self.maxRecipe(recipe, self.listTotalBerry))
            listAllRecipe.append(recipe)
        return listAllRecipe

    @staticmethod
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

    def buildAllPossibilities(self):
        listAllPossibilities = []
        for i, recipe in enumerate(self.listAllRecipe):
            print(recipe)
            listAllPossibilities.append([])
            for number in range(recipe[4] + 1):
                listAllPossibilities[i].append(self.berryUsedPerMultipleIteration(recipe, number))
        return listAllPossibilities

    @staticmethod
    def berryUsedPerMultipleIteration(recipe, number):
        a, b, c, n, m = recipe
        return [a * number, b * number, c * number]


class Counter:
    def __init__(self, listAllRecipe: AllRecipe):
        self.counter = self.buildCounter(listAllRecipe.listAllRecipe)

    @staticmethod
    def buildCounter(listAllRecipe):
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

    def isEmpty(self):
        return self.counterToString() == "0" * len(self.counter)

    def plus1ToCounter(self):
        for recipeIndex in self.counter[::-1]:
            recipeIndex[0] += 1
            if not recipeIndex[0] > recipeIndex[1]:
                return True
            recipeIndex[0] = 0
        # If the counter get to the initial position
        return False

    # TODO c'est tres sus comme technique faire gaffe aux reset pas et qui fait des boucles infinies
    def getToPreviousRecipe(self):
        for index in range(len(self.counter) - 1, -1, -1):
            if self.counter[index][0]:
                self.counter[index][0] = 0
                for indexRecipeCounterToReset in range(index - 1, -1, -1):
                    recipeCounter = self.counter[indexRecipeCounterToReset]
                    if recipeCounter[0] == recipeCounter[1]:
                        recipeCounter[0] = 0
                    else:
                        recipeCounter[0] += 1
                        break
                break


result = ""
print(result)

# TODO condition d'arret
run = True
progDyna = {}

while run:
    run = False

allRecipe = AllRecipe()

counter = Counter(allRecipe)

print(counter.counterToString())
print("1_______________________")
for _ in range(67):
    counter.plus1ToCounter()

print(counter.counterToString())
counter.getToPreviousRecipe()
print(counter.counterToString())

# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepct ----> <|{outputExpected}|>")
