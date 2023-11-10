import sys, io
from testVisu import show

sampleToTest = "1"
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

    def getLast(self):
        return self.pile[-1]


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


def lockResetCell(x, y, end=False):
    a = "test"
    # todo enregistrer le max
    if x == width - 1 and y == height - 1:
        gridParcours[height - 1][width - 1] = [True, True, True, True]
        if end:
            # todo ajouter une comparaison entre les arbres a cut mini et la coupe courante
            print("je suis a la fin")
        return

    lockside(x, y, LEFT, x == 0, False)
    lockside(x, y, RIGHT, x == width - 1, False)
    lockside(x, y, TOP, y == 0, False)
    lockside(x, y, BOTTOM, y == height - 1, False)


def lockside(x, y, side, ban, alert=True):
    if not isValidToVisit(x, y, side) and alert:
        print("i am stuck")
    gridParcours[y][x][side] = ban


def isValidToVisit(x, y, side):
    if gridParcours[y][x][side]:
        return False
    return True


def isAlreadyVisited(cell):
    if cell in pile.pile:
        return True
    return False


def rollBackToPreviousCell():
    actualCell = pile.depile()
    lockResetCell(*actualCell, True)
    return pile.getLast()


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
    a = "test"
    for side in range(4):
        if isValidToVisit(x, y, side):
            newCoords = findCoordsByASide(x, y, side)
            if not isAlreadyVisited(newCoords):
                return *newCoords, side
    return False


# todo check le hplanner en fx de la liste de parcours a la place de compter si besoins
def mooveToNextCell(xCurrent, yCurrent, hPlanneur):
    tupleResultSide = chooseSideToGo(xCurrent, yCurrent)
    # todo faire un rollback si trop d'arbres a couper par rapport au mini
    if tupleResultSide:
        hPlanneur -= 1
        xNew, yNew, side = tupleResultSide
        # On bloque la possibilité d'aller à la case où l'on va
        lockside(xCurrent, yCurrent, side, True)
        # On prend le côté opposé
        reversedSide = reverseSide(side)
        # On bloque la possibilité d'aller à la case où l'on est actuellement
        lockside(xNew, yNew, reversedSide, True)
        # On enregistre la case ou l'on se dirige
        pile.empile(xNew, yNew)
        # on coupe ce qui dépasse de l'arbre
        treeHeight = gridForest[yNew][xNew]
        # todo fix that shit
        meterToCut = max(0,treeHeight-hPlanneur)
        # On enregistre le déplacement
        return xNew, yNew, hPlanneur
    else:
        print('je rollback')
        return *rollBackToPreviousCell(), hPlanneur + 1


def reverseSide(side):
    return (side + 2) % 4


# TODO check a chaque moove qu'il y a assez de reach pour atteindre la sortie
def voyage(hPlanneur):
    numberOfMeterToCut = 0
    xCurrent, yCurrent = 0, 0
    pile.empile(xCurrent, yCurrent)
    for numberOfMoove in range(nombreMOOVE):
        try:
            xCurrent, yCurrent, hPlanneur = mooveToNextCell(xCurrent, yCurrent, hPlanneur)
        except IndexError:
            # todo add return here
            # return numberOfMeterToCut
            print("numberOfMeterToCut", numberOfMeterToCut)
            print("numberOfMoove", numberOfMoove)
            break
    print("hPlanneur", hPlanneur)
    print("pile", pile.pile)
    for line in gridParcours:
        print(line)
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
gridParcours = []

for yh in range(height):
    gridParcours.append([])
    for xw in range(width):
        gridParcours[yh].append([False, False, False, False])
        lockResetCell(xw, yh)

pile = Pile()
nombreMOOVE = 900000
voyage(hPlanneur)

result = ""
print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepct ----> <|{outputExpected}|>")
