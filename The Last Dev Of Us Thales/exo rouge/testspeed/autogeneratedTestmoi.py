import timeit
aTester = """
import sys, io

sampleToTest = "9"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

class Node:
    def __init__(self, value=False):
        self.value = value
        self.false = None
        self.true = None


class binaryTree:
    def __init__(self, numberOfGene):
        self.root = self.buildTree(numberOfGene)

    @staticmethod
    def buildTree(numberOfGene):
        arrayTree = []
        numberOfPossibilities = 2 ** (numberOfGene + 1) - 1
        arrayTree.append(Node("Root"))
        for i in range(1, numberOfPossibilities):
            arrayTree.append(Node())
            parent_index = (i - 1) // 2
            if i % 2 == 0:
                arrayTree[parent_index].false = arrayTree[i]
            else:
                arrayTree[parent_index].true = arrayTree[i]
        return arrayTree[0]

    def getNextNode(self, bool, node=None):
        if node is None:
            node = self.root
        if bool:
            return node.true
        return node.false

    # for debug purpose only or if you want to understand how this is work
    def print_tree(self, node="root", level=0):
        if node == "root":
            node = self.root
        if node is None:
            return
        self.print_tree(node.false, level + 1)
        print("    " * level + str(node.value))
        self.print_tree(node.true, level + 1)


def reverse(string):
    return string[::-1]


def binToIndex(arrayBin):
    return ''.join(map(str, arrayBin))


def fusion(geneA, geneB):
    strMini = geneA + geneB
    nbMini = len(strMini)
    for indexRight in range(len(geneB), 0, -1):
        partB = geneB[:indexRight]
        if geneA.endswith(partB):
            stringFusion = geneA[:-len(partB)] + geneB
            lenFusion = len(stringFusion)
            if nbMini > lenFusion:
                strMini = stringFusion
                break
    return strMini


numberOfGene = int(input())
numberOfPossibilities = 2 ** numberOfGene
binaryTree = binaryTree(numberOfGene)

stringResult = input()
countResult = len(stringResult)
listGene = stringResult.split(" ")

for numberOfIteration in range(numberOfPossibilities):

    pattern = list(map(int, bin(numberOfIteration)[2:].zfill(numberOfGene)))

    actualGeneBase = binaryTree.getNextNode(pattern[0])
    if not actualGeneBase.value:
        if not pattern[0]:
            actualGeneBase.value = listGene[0]
        else:
            actualGeneBase.value = reverse(listGene[0])
    geneA = actualGeneBase.value

    for indexGeneA in range(len(pattern) - 1):
        indexGeneB = indexGeneA + 1
        actualGeneBase = binaryTree.getNextNode(pattern[indexGeneB], actualGeneBase)
        if not actualGeneBase.value:
            geneB = listGene[indexGeneB]
            if pattern[indexGeneB]:
                geneB = reverse(geneB)
            actualGeneBase.value = fusion(geneA, geneB)
        geneA = actualGeneBase.value
        lenFusion = len(geneA)
        if countResult < lenFusion:
            lenFusion = -1
            break
    if countResult > lenFusion != -1:
        countResult = lenFusion
        stringResult = geneA
print(stringResult)
# binaryTree.print_tree()
"""
execution_time = timeit.timeit(aTester, number=1000)
print(f"Temps d'exécution moyen : {execution_time} secondes")