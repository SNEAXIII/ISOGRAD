from collections import defaultdict

V, E = map(int, input().split())

D = defaultdict(set)

for _ in range(E):
    u, v = input().split()
    D[u].add(v)

for u, a in D.items():
    if len(a) != 1: continue
    v, = a
    if v in D and len(D[v]) == V - 2 and u not in D[v]:
        print(u)
        break
