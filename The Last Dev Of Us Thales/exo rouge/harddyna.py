import sys, io
from _ast import pattern

sampleToTest = "Custom"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


# START
class Node:
    def __init__(self, value):
        self.value = value
        self.false = None
        self.true = None

    def __str__(self):
        return f"({self.false})<--{self.value}-->({self.true})"


class binaryTree:

    def __init__(self, nombreGene):
        self.root = self.buildTree(nombreGene)

    @staticmethod
    def buildTree(nombreGene):
        tree = []
        nombrePossibilite = 2 ** nombreGene - 1
        for i in range(nombrePossibilite):
            tree.append(Node(False))

        # Construction de l'arbre en établissant les relations entre les nœuds
        for i in range(1, len(tree)):
            parent_index = (i - 1) // 2
            if i % 2 == 0:
                tree[parent_index].false = tree[i]
            else:
                tree[parent_index].true = tree[i]
        return tree[0]


def reverse(string):
    return string[::-1]


def binToIndex(arrayBin):
    return ''.join(map(str, arrayBin))


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
binaryTree = binaryTree(numberOfGene)

stringResult = input()
countResult = len(stringResult)
listGene = stringResult.split(" ")

progDynamique = []

for numberOfIteration in range(valMaxi):
    progDynamique.append(False)
    pattern = list(map(int, bin(numberOfIteration)[2:].zfill(numberOfGene)))
    # pattern = [(numberOfIteration >> i) & 1 for i in range(numberOfGene)]
    geneA = listGene[0]
    if pattern[0]:
        geneA = reverse(geneA)
    for indexGeneA in range(len(pattern) - 1):
        indexGeneB = indexGeneA + 1
        print(binToIndex(pattern[0:indexGeneB + 1]))
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
