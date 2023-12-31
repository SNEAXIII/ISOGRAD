import sys, io
from testVisu import show

sampleToTest = "4"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = int(f.read())
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

# START
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class PileCuttingTree:
    def __init__(self):
        self.pile = []

    def depile(self):
        return self.pile.pop()

    def empile(self, h):
        self.pile.append(h)

    def getLast(self):
        return self.pile[-1]

    def getCurrentMeterToCut(self):
        return self.getLast()


class PileParcours:
    def __init__(self):
        self.pile = []

    def depile(self):
        return self.pile.pop()

    def empile(self, x, y):
        self.pile.append((x, y))

    def getLast(self):
        return self.pile[-1]

    def getHRestant(self):
        return hMaxPlanneur - len(self.pile)


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
    if x == width - 1 and y == height - 1:
        gridParcours[height - 1][width - 1] = [True, True, True, True]
        if end:
            # print("je suis a la fin")
            print(pileParcours.pile)
            print(pileCuttingTree.getCurrentMeterToCut())
            global result
            if pileCuttingTree.getCurrentMeterToCut() == 0:
                result = pileCuttingTree.getCurrentMeterToCut()
                raise TimeoutError()
            elif result is not None:
                result = min(result, pileCuttingTree.getCurrentMeterToCut())
            else:
                result = pileCuttingTree.getCurrentMeterToCut()
        return

    lockside(x, y, LEFT, x == 0, False)
    lockside(x, y, RIGHT, x == width - 1, False)
    lockside(x, y, TOP, y == 0, False)
    lockside(x, y, BOTTOM, y == height - 1, False)


def lockside(x, y, side, ban, alert=True):
    # if not isValidToVisit(x, y, side) and alert:
    #     print("i am stuck")
    gridParcours[y][x][side] = ban


def isValidToVisit(x, y, side):
    if gridParcours[y][x][side]:
        return False
    return True


def isAlreadyVisited(cell):
    if cell in pileParcours.pile:
        return True
    return False


def rollBackToPreviousCell():
    x, y = pileParcours.depile()
    pileCuttingTree.depile()
    lockResetCell(x, y, True)
    return pileParcours.getLast()


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
    # todo bug incoming, vérifier l'excactitude des mesures de fin de parcours
    if result:
        isTooMuchToCut = result < pileCuttingTree.getLast()
        if isTooMuchToCut:
            return False
    isNotEnoughReach = not isEnoughReachToJoinTheExit(width, height, pileParcours.getHRestant())
    if isNotEnoughReach:
        return False
    for side in range(4):
        if isValidToVisit(x, y, side):
            newCoords = findCoordsByASide(x, y, side)
            if not isAlreadyVisited(newCoords):
                return *newCoords, side
    return False


def mooveToNextCell(xCurrent, yCurrent):
    tupleResultSide = chooseSideToGo(xCurrent, yCurrent)
    # todo faire un rollback si trop d'arbres a couper par rapport au mini
    if tupleResultSide:
        hPlanneur = pileParcours.getHRestant()
        xNew, yNew, side = tupleResultSide
        # On bloque la possibilité d'aller à la case où l'on va
        lockside(xCurrent, yCurrent, side, True)
        # On prend le côté opposé
        reversedSide = reverseSide(side)
        # On bloque la possibilité d'aller à la case où l'on est actuellement
        lockside(xNew, yNew, reversedSide, True)
        # on coupe ce qui dépasse de l'arbre
        treeHeight = gridForest[yNew][xNew]
        meterToCut = max(0, treeHeight - hPlanneur)
        currentMeterToCut = pileCuttingTree.getCurrentMeterToCut() + meterToCut
        # On enregistre le déplacement
        pileCuttingTree.empile(currentMeterToCut)
        pileParcours.empile(xNew, yNew)
        return xNew, yNew
    else:
        # print('je rollback')
        return rollBackToPreviousCell()


def reverseSide(side):
    return (side + 2) % 4


# TODO check a chaque moove qu'il y a assez de reach pour atteindre la sortie
def voyage():
    curentNumberOfMeterToCut = 0
    pileCuttingTree.empile(curentNumberOfMeterToCut)
    xCurrent, yCurrent = 0, 0
    pileParcours.empile(xCurrent, yCurrent)
    for numberOfMoove in range(nombreMOOVE):
        # if numberOfMoove % 200000 == 0:
        #     print("numberOfMoove",numberOfMoove)
        try:
            xCurrent, yCurrent = mooveToNextCell(xCurrent, yCurrent)
        except IndexError:
            break
        except TimeoutError:
            return 0
    # printGrid(xCurrent, yCurrent)
    return result
    # for line in gridParcours:
    #     print(line)
    #


width, height = map(int, input().split())
hMaxPlanneur = int(input())

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

pileCuttingTree = PileCuttingTree()
pileParcours = PileParcours()
result = None

nombreMOOVE = 999999999

print(voyage())
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepect ----> <|{outputExpected}|>")
