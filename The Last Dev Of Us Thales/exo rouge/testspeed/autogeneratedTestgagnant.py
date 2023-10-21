import timeit
aTester = """
import sys, io

sampleToTest = "9"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\\n'))

def solve(pieces):
    import itertools
    n = len(pieces)
    res = ''.join(pieces)
    for fliplist in itertools.product((-1,1), repeat=n):
        s = pieces[0][::fliplist[0]]
        for i in range(1, n):
            piece = pieces[i][::fliplist[i]]
            for overlap in range(min(len(piece), len(s))-1, -1, -1):
                if s[-overlap:] == piece[:overlap]:
                    break
            s += piece[overlap:]
        if len(s) < len(res):
            res = s
    return res

print(solve(lines[1].split()))

"""
execution_time = timeit.timeit(aTester, number=1000)
print(f"Temps d'exécution moyen : {execution_time} secondes")