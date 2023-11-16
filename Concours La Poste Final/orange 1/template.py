import sys, io

sampleToTest = "Custom"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START
result = ""
lStatue, hStatue, lSalle, hSalle = map(int, input().split(" "))

lines = [input() for _ in range(hSalle)]
linesDyna = []
for indexLine,line in enumerate(lines):
    print("______________________")
    count = 0
    linesDyna.append(set())
    for index,space in enumerate(line):
        if space == ".":
            count += 1
        elif space == "#":
            count = 0
        if count >= lStatue+2:
            linesDyna[indexLine].add(index)
            print(index)
print(linesDyna)

print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|\n{result}\n|>\nexepect ----> <|\n{outputExpected}\n|>")
