

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
            # TODO REMOVE THIS SHIT
            # print(recipe)
            listAllPossibilities.append([])
            for number in range(recipe[4] + 1):
                listAllPossibilities[i].append(self.berryUsedPerMultipleIteration(recipe, number))
        return listAllPossibilities

    def getByPossibilitie(self, counter):
        result = []
        for index, recipe in enumerate(counter):
            result.append(self.allPossibilities[index][recipe[0]])
        return result

    @staticmethod
    def berryUsedPerMultipleIteration(recipe, number):
        a, b, c, n, m = recipe
        return [a * number, b * number, c * number]

    def isPossibleToCraft(self, counter):
        currentPossibilities = self.getByPossibilitie(counter.counter)
        sumA = sum(recipe[0] for recipe in currentPossibilities)
        sumB = sum(recipe[1] for recipe in currentPossibilities)
        sumC = sum(recipe[2] for recipe in currentPossibilities)
        maxA, maxB, maxC = self.listTotalBerry
        if sumA <= maxA and sumB <= maxB and sumC <= maxC:
            return counter
        return False

    def getMaxNrjByRecipe(self, counter):
        return sum(counter.counter[index][0] * self.listAllRecipe[index][3] for index in range(len(counter.counter)))


class Counter:
    def __init__(self, listAllRecipe: AllRecipe):
        self.listAllRecipe = listAllRecipe
        self.counter = self.buildCounter()

    def buildCounter(self):
        counter = []
        for recipe in self.listAllRecipe.listAllRecipe:
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

    def isFilled(self):
        return self.counterToString() != "0" * len(self.counter)

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


allRecipe = AllRecipe()
counter = Counter(allRecipe)
intResult = 0
strResult = []
# TODO condition d'arret
run = True
while counter.plus1ToCounter() and run:
    if counter.listAllRecipe.isPossibleToCraft(counter):
        nrjTry = counter.listAllRecipe.getMaxNrjByRecipe(counter)
        if nrjTry > intResult:
            intResult = nrjTry
            strResult = "".join(str(recipe[0]) for recipe in counter.counter)
    else:
        counter.getToPreviousRecipe()

    run = counter.isFilled()
print(intResult)
print(strResult)
# TODO print result
# print(result)
