import timeit
aTester = r"""
import sys, io

sampleToTest = "11"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
lStatue, hStatue, lSalle, hSalle = map(int, input().split(" "))


def multiIntersect(y):
    intersect = linesPosition[y]
    for line in linesPosition[y + 1:y + 1 + hStatue]:
        intersect &= line
        if not intersect:
            return False
    return intersect.pop()


def fillGrid(x, y):
    for index in range(hStatue):
        copyLines = lines[y + index + 1]
        lines[y + index + 1] = copyLines[:x] + "x" * lStatue + copyLines[x + lStatue:]


def findLocation():
    for y in range(hSalle - hStatue):
        location = multiIntersect(y)
        if location:
            fillGrid(location, y)
            break


lines = [input() for _ in range(hSalle)]

linesPosition = []
for y, yElem in enumerate(lines):
    count = 0
    linesPosition.append(set())
    for x, xElem in enumerate(yElem):
        if xElem == ".":
            count += 1
        else:
            count = 0
        if count >= lStatue + 2:
            linesPosition[y].add(x - lStatue)

findLocation()

# for line in lines:
#     print(line)
"""
execution_time = timeit.timeit(aTester, number=100)
print(f"Temps d'exécution moyen : {execution_time} secondes")