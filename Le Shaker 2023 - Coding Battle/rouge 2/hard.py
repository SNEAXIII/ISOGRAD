import sys, io
from testVisu import show

sampleToTest = "Custom"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

# START
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class Pile:
    def __init__(self):
        self.pile = []

    def depile(self):
        return self.pile.pop()

    def empile(self, x, y):
        self.pile.append((x, y))


def printGrid(xCurrent, yCurrent):
    show(gridForest, xCurrent, yCurrent)


def addTree(xTree, yTree, hTree):
    gridForest[yTree][xTree] = hTree


def addMultiTree():
    n = int(input())
    for _ in range(n):
        pass
        xTree, yTree, hTree = map(int, input().split())
        addTree(xTree, yTree, hTree)


def isEnoughReachToJoinTheExit(x, y, h):
    return width - x + height - y - 2 <= h


def lockResetCell(x, y):
    if x == 0:
        lockside(x, y, LEFT, False)
    if x == width - 1:
        lockside(x, y, RIGHT, False)
    if y == 0:
        lockside(x, y, TOP, False)
    if y == height - 1:
        lockside(x, y, BOTTOM, False)


def lockside(x, y, side, alert=True):
    if not isValidToVisit(x, y, side) and alert:
        print("ALEEEEED")
    gridParcours[y][x][side] = 1


def isValidToVisit(x, y, side):
    if gridParcours[y][x][side]:
        return False
    return True


def isAlreadyVisited(cell):
    if cell in pile.pile:
        return True
    return False


def findCoordsByASide(x, y, side):
    if side == 0:
        y -= 1
    elif side == 1:
        x += 1
    elif side == 2:
        y += 1
    elif side == 3:
        x -= 1
    return x, y


def chooseSideToGo(x, y):
    for side in range(4):
        if isValidToVisit(x, y, side):
            newCoords = findCoordsByASide(x, y, side)
            if not isAlreadyVisited(newCoords):
                return *newCoords, side
    return False


def mooveToNextCell(xCurrent, yCurrent):
    xNew, yNew, side = chooseSideToGo(xCurrent, yCurrent)
    # On bloque la possibilité d'aller à la case ou l'on va
    lockside(xCurrent, yCurrent, side)
    # On prends le coté opposé
    reversedSide = reverseSide(side)
    # On bloque la possibilité d'aller à la case ou l'on est actuellement
    lockside(xNew, yNew, reversedSide)
    # On enregistre la case ou l'on se dirige
    pile.empile(xNew, yNew)
    # On enregistre le déplacement
    return xNew, yNew

def reverseSide(side):
    return (side + 2) % 4


def voyage(hPlanneur):
    xCurrent, yCurrent = 0, 0
    pile.empile(xCurrent, yCurrent)
    # todo start fix
    xCurrent, yCurrent = mooveToNextCell(xCurrent, yCurrent)
    xCurrent, yCurrent = mooveToNextCell(xCurrent, yCurrent)
    xCurrent, yCurrent = mooveToNextCell(xCurrent, yCurrent)
    xCurrent, yCurrent = mooveToNextCell(xCurrent, yCurrent)
    # todo end fix
    print(hPlanneur)
    print(pile.pile)
    printGrid(xCurrent, yCurrent)


# TODO montrer au prof l'erreur qu'il a remarque sur le jeu numéro 2
width, height = map(int, input().split())
hPlanneur = int(input())



# Si le parcours est impossible
# TODO remettre plus tard si il le faut
# if not isEnoughReachToJoinTheExit(width, height, hPlanneur):
#     printGrid()
#     print("impossible")
#     exit()

gridForest = [[0 for _ in range(width)] for _ in range(height)]

addMultiTree()
# todo faire un fonction pour déterminer un coté ou partir
# todo faire une fonction pour savoir si on est deja allé
# todo faire un roll back
gridParcours = []

for yh in range(height):
    gridParcours.append([])
    for xw in range(width):
        gridParcours[yh].append([0, 0, 0, 0])
        lockResetCell(xw, yh)

for line in gridParcours:
    print(line)

pile = Pile()

voyage(hPlanneur)

result = ""
print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepct ----> <|{outputExpected}|>")
