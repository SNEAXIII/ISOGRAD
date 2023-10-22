nbGene = 3
nombrePossibilite = 2 ** nbGene
progDynamique = [False for _ in range(nombrePossibilite)]


def binToIndex(arrayBin):
    return int(''.join(map(str, arrayBin)), base=2)

x=5
pattern = list(map(int, bin(x)[2:].zfill(5)))
print(binToIndex(pattern))
