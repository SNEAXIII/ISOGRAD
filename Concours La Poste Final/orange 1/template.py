import sys, io

sampleToTest = "Custom2"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START
result = ""
lStatue, hStatue, lSalle, hSalle = map(int, input().split(" "))

lines = [input() for _ in range(hSalle)]
linesDyna = []
colonnesDyna = []
print("les lignes")
for y, yElem in enumerate(lines):
    print("______________________")
    count = 0
    linesDyna.append(set())
    for x, xElem in enumerate(yElem):
        if xElem == ".":
            count += 1
        elif xElem == "#":
            count = 0
        if count >= lStatue + 2:
            xGood = x - lStatue
            linesDyna[y].add(xGood)
            print(xGood)

print("les collones")
for x in range(lSalle):
    print("______________________")
    count = 0
    colonnesDyna.append(set())
    for y in range(hSalle):
        case = lines[y][x]
        if case == ".":
            count += 1
        elif case == "#":
            count = 0
        if count >= hStatue + 2:
            yGood = y - hStatue
            colonnesDyna[x].add(yGood)
            print(xGood)

print(linesDyna)
print(colonnesDyna)


print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|\n{result}\n|>\nexepect ----> <|\n{outputExpected}\n|>")
