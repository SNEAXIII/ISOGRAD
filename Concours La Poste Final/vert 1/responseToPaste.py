sides = list(map(int, (input(), input(), input())))

hypo = max(sides)
sides.pop(sides.index(hypo))
maxi = sides.pop() ** 2
maxi += sides.pop() ** 2

if maxi == hypo ** 2:
    result = "OUI"
else:
    result = "NON"

print(result)
