import sys, io

sampleToTest = "4"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
# START
def check():
    result = ""
    ancienIndex2 = 0
    for cara1 in motif1:
        indexCara2 = motif2.find(cara1)
        if not indexCara2 == -1:
            if ancienIndex2 > indexCara2:
                return False
            else:
                result += cara1
                ancienIndex2 = indexCara2
    if result:
        return result
    return False

motif1 = input()

motif2 = input()

result = check()
if result:
    result = f"TEMPETE\n{result}"
    print(result)
else:
    result = "NORMAL"
    print(result)


# END
if outputExpected == result:
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide\noutput ----> <|{result}|>\nexepect ----> <|{outputExpected}|>")
