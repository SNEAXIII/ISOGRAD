import sys, io
from testVisu import main

sampleToTest = "2"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START

def printGrid():
    main(gridForest)


def addTree(xTree, yTree, hTree):
    gridForest[yTree][xTree] = hTree


def addMultiTree():
    n = int(input())
    for _ in range(n):
        pass
        xTree, yTree, hTree = map(int, input().split())
        addTree(xTree, yTree, hTree)


def isEnoughReachToJoinTheExit(x, y, h):
    return x + y - 2 <= h


def coordinate_to_index(x, y, height):
    return y * height + x


# TODO montrer au prof l'erreur qu'il a remarque sur le jeu numéro 2
width, height = map(int, input().split())
h = int(input())
print(h)

# Si le parcours est impossible
if not isEnoughReachToJoinTheExit(width, height, h):
    printGrid()
    print("impossible")
    exit()

gridForest = [[0] * width] * height

addMultiTree()
# todo faire une matrice des coté emprunté pour chaque cases individuelles
# todo faire un fonction pour déterminer un coté ou partir
# todo faire une fonction pour savoir si on est deja allé
# todo faire un roll back
gridParcours = [[[0] * 4] * width] * height
for line in gridParcours:
    print(line)

# todo faire un set des case déja parcourues
printGrid()

result = ""
print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepct ----> <|{outputExpected}|>")
