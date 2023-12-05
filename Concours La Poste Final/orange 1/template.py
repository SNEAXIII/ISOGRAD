import sys, io

sampleToTest = "Custom2"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START
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

for line in lines:
    print(line)
# END
result = ""
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|\n{result}\n|>\nexepect ----> <|\n{outputExpected}\n|>")
