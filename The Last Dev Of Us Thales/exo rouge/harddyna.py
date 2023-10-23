import sys, io

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
        return f"{self.false})<--{self.value}-->({self.true})"

    def setValue(self, value):
        self.value = value



class binaryTree:
    def __init__(self, nombreGene):
        self.root = self.buildTree(nombreGene)

    @staticmethod
    def buildTree(nombreGene):
        tree = []
        nombrePossibilite = 2 ** nombreGene - 1
        tree.append(Node("Root"))
        # Construction de l'arbre en établissant les relations entre les nœuds
        for i in range(1, nombrePossibilite):
            tree.append(Node(False))
            parent_index = (i - 1) // 2
            if i % 2 == 0:
                tree[parent_index].false = tree[i]
            else:
                tree[parent_index].true = tree[i]
        return tree[0]

    def getNextNode(self, bool, node = None):
        if node is None:
            node = self.root
        if bool:
            return node.true
        return node.false


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

for numberOfIteration in range(valMaxi):

    pattern = list(map(int, bin(numberOfIteration)[2:].zfill(numberOfGene)))
    # pattern = [(numberOfIteration >> i) & 1 for i in range(numberOfGene)]

    actualGeneBase = binaryTree.getNextNode(pattern[0])
    if not actualGeneBase.value:
        if not pattern[0]: actualGeneBase.value = listGene[0]
        else: actualGeneBase.value = reverse(listGene[0])
    geneA = actualGeneBase.value

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
