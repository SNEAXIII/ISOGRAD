import sys, io

sampleToTest = "6"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = int(f.read())
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START

result = int(input())

for _ in range(4):
    if result % 3 == 0:
        result //= 3
    elif result % 2 == 0:
        result //= 2
    else:
        result -= 1

print(result)
# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepect ----> <|{outputExpected}|>")
