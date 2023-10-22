import sys, io
from _ast import pattern

sampleToTest = "9"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START
def reverse(string):
    return string[::-1]


def fusion(genes):
    geneA, geneB = genes
    strMini = geneA + geneB
    nbMini = len(strMini)
    for indexRight in range(len(geneB), 0, -1):
        partB = geneB[:indexRight]
        if geneA.endswith(partB):
            stringFusion = geneA[:-len(partB)] + geneB
            lenFusion = len(stringFusion)
            if lenFusion != nbMini:
                if nbMini > lenFusion:
                    nbMini, strMini = lenFusion, stringFusion
                break
            if lenFusion in (len(geneA), len(geneB)):
                return stringFusion, lenFusion

    return strMini, nbMini


numberOfGene = int(input())
valMaxi = 2 ** numberOfGene

stringResult = input()
countResult = len(stringResult)
listGene = stringResult.split(" ")

for numberOfIteration in range(valMaxi):
    pattern = list(map(int, bin(numberOfIteration)[2:].zfill(numberOfGene)))
    # pattern = [(numberOfIteration >> i) & 1 for i in range(numberOfGene)]
    geneA = listGene[0]
    if pattern[0]:
        geneA = reverse(geneA)
    for indexGeneA in range(len(pattern) - 1):
        indexGeneB = indexGeneA + 1
        geneB = listGene[indexGeneB]
        if pattern[indexGeneB]:
            geneB = reverse(geneB)
        geneA, lenFusion = fusion((geneA, geneB))
        if countResult < lenFusion:
            lenFusion = -1
            break
    if countResult > lenFusion != -1:
        countResult = lenFusion
        stringResult = geneA
print(stringResult)
# END

if len(outputExpected) == len(stringResult):
    print("Le test est valide")
else:
    print(f"Le test n'est pas valide --> output = {len(stringResult)} contre exepct = {len(outputExpected)}")
