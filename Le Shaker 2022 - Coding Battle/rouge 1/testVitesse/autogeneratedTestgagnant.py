import timeit
aTester = """
import sys, io

sampleToTest = "4"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
A, B, C = map(int, input().split())
N = int(input())
recipes = []
for i in range(N):
    recipes.append(tuple(map(int, input().split())))

NRJ = [[[0 for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(A + 1)]
rec_used = [[[-1 for _ in range(C + 1)] for _ in range(B + 1)] for _ in range(A + 1)]

best_nrj_tot = 0
best_comp = (0, 0, 0)

for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):

            best_nrj = 0
            best_rcp = -1

            for n in range(N):
                ra, rb, rc, nrj = recipes[n]

                if ra > a or rb > b or rc > c:
                    continue

                new_nrj = NRJ[a - ra][b - rb][c - rc] + nrj

                if new_nrj > best_nrj:
                    best_nrj = new_nrj
                    best_rcp = n

            NRJ[a][b][c] = best_nrj
            rec_used[a][b][c] = best_rcp

            if best_nrj > best_nrj_tot:
                best_nrj_tot = best_nrj
                best_comp = (a, b, c)

sol_rec = [0 for _ in range(N)]
a, b, c = best_comp
while rec_used[a][b][c] > -1:
    sol_rec[rec_used[a][b][c]] += 1
    ra, rb, rc, _ = recipes[rec_used[a][b][c]]
    a -= ra
    b -= rb
    c -= rc

print(best_nrj_tot, *sol_rec, sep='\\n')
"""
execution_time = timeit.timeit(aTester, number=1000)
print(f"Temps d'exécution moyen : {execution_time} secondes")