import sys, io

sampleToTest = "2"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START

def printMap():
    for line in gridForest:
        print(line)


def addTree(xTree, yTree, hTree):
    gridForest[yTree][xTree] = hTree


def addMultiTree():
    n = int(input())
    print(n)
    for _ in range(n):
        pass
        xTree, yTree, hTree = map(int, input().split())
        addTree(xTree, yTree, hTree)


def ifNotEnoughReachToJoinTheExit(x, y, h):
    return x+y-1>=h

x, y = map(int, input().split())
h = int(input())
gridForest = [[0 for _ in range(x)] for _ in range(y)]

addMultiTree()

printMap()

result = ""
print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepct ----> <|{outputExpected}|>")
