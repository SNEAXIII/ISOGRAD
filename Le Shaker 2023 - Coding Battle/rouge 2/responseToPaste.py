TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3


class Pile:
    def __init__(self):
        self.pile = []

    def depile(self):
        return index_to_coordinate(self.pile.pop())

    def empile(self, elem):
        self.pile.append(coordinate_to_index(elem))


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


def coordinate_to_index(x, y):
    return y * height + x


def index_to_coordinate(index):
    return index % height, index // height


def lockResetAll():
    for y in range(height):
        for x in range(width):
            index = coordinate_to_index(x, y)
            lockResetCell(index)


def lockResetCell(index):
    x, y = index_to_coordinate(index)
    if x == 0:
        lockside(x, y, LEFT)
    if x == width - 1:
        lockside(x, y, RIGHT)
    if y == 0:
        lockside(x, y, TOP)
    if y == height - 1:
        lockside(x, y, BOTTOM)


def lockside(x, y, side):
    if not isValidSide(x, y, side):
        print("ALEEEEED")
    gridParcours[y][x][side] = 1

def isValidSide(x, y, side):
    if gridParcours[y][x][side]:
        return False
    return True


# TODO montrer au prof l'erreur qu'il a remarque sur le jeu numéro 2
width, height = map(int, input().split())
h = int(input())
print(h)

# Si le parcours est impossible
if not isEnoughReachToJoinTheExit(width, height, h):
    printGrid()
    print("impossible")
    exit()

gridForest = [[0 for _ in range(width)] for _ in range(height)]

addMultiTree()
# todo faire un fonction pour déterminer un coté ou partir
# todo faire une fonction pour savoir si on est deja allé
# todo faire un roll back
gridParcours = [[[0, 0, 0, 0] for _ in range(width)] for _ in range(height)]

lockResetAll()

# todo faire une pile des case déja parcourues
printGrid()

result = ""
print(result)
