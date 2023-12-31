import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n, m, l, h = map(int, lines[0].split())
grid = list(map(list, lines[1:]))
sol = None
solcnt = 0
for rbase in range(h - m - 1):
    for cbase in range(l - n - 1):
        good = True
        for r in range(rbase, rbase + m + 2):
            for c in range(cbase, cbase + n + 2):
                if grid[r][c] == '#':
                    good = False
        if good:
            solcnt += 1
            sol = (rbase, cbase)

assert sol is not None

for r in range(sol[0] + 1, sol[0] + m + 1):
    for c in range(sol[1] + 1, sol[1] + n + 1):
        grid[r][c] = 'x'
# for row in grid:
#     print(''.join(row))
