import timeit
aTester = """
import sys, io

sampleToTest = "9"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

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
valMaxi = 2 ** numberOfGene - 1

stringResult = input()
countResult = len(stringResult)
listGene = stringResult.split(" ")

numberOfIteration = 0

while numberOfIteration <= valMaxi:
    pattern = list(map(int, bin(numberOfIteration)[2:].zfill(numberOfGene)))
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
    numberOfIteration += 1
print(stringResult)
"""
execution_time = timeit.timeit(aTester, number=1000)
print(f"Temps d'exécution moyen : {execution_time} secondes")