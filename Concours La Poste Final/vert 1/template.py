import sys, io


sampleToTest = "1"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START
sides = list(map(int, (input(), input(), input())))

hypo = max(sides)
sides.pop(sides.index(hypo))
maxi = sides.pop() ** 2
maxi += sides.pop() ** 2

if maxi == hypo ** 2:
    result = "OUI"
else:
    result = "NON"

print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepect ----> <|{outputExpected}|>")
