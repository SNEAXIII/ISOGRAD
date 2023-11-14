import timeit
aTester = r"""
import sys, io

sampleToTest = "3"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


from collections import Counter

def main():
    N, V = map(int, input().split())
    parents: list[None|int] = [None]*V
    for _ in range(N):
        a,b = map(int, input().split())
        parents[b]=a
    leaves = set(range(V)) - set(parents)
    count = Counter()
    for i in leaves:
        root = i
        while parents[root] is not None:
            root = parents[root]
        count[root]+=1
    print(count.most_common(1)[0][0])

main()

"""
execution_time = timeit.timeit(aTester, number=10000)
print(f"Temps d'exécution moyen : {execution_time} secondes")