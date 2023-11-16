from math import sqrt

sides = set(map(int, (input(), input(), input())))

hypo = max(sides)
sides.discard(hypo)
maxi = sides.pop() ** 2
maxi += sides.pop() ** 2

if round(sqrt(maxi), 1) == round(hypo, 1):
    result = "OUI"
else:
    result = "NON"

print(result)
