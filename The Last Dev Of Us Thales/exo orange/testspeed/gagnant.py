import timeit

aTester = """
import sys, io

with open(f"output11.txt") as f:
    outputexepct = int(f.read())
with open(f"input11.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\\n'))

def convert(s):
    h, m = map(int, s.split(':'))
    return 60 * h + m

n = lines[0]
prev = []
res = 0
for line in lines[1:]:
    t1, t2 = map(convert, line.split(' - '))
    timeset = set(range(t1, t2))
    for other in prev:
        if len(timeset & other) >= 15:
            res += 1
    prev.append(timeset)
"""

execution_time = timeit.timeit(aTester, number=1000)

print(f'Temps d\'exécution moyen : {execution_time} secondes')