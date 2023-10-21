import timeit

aTester = """
import sys, io

with open(f"output11.txt") as f:
    outputexepct = int(f.read())
with open(f"input11.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())


def convert(string):
    hour,minute = map(int,string.split(":"))
    return hour * 60 + minute


nbSurvivor = int(input())

allSurvivor = [list(map(convert, input().split(" - "))) for _ in range(nbSurvivor)]

allSurvivor.sort(key=lambda x: x[0])

result = 0
dansSalle = []

for personneEntrante in allSurvivor:
    personneSortant = []
    minuteArriveeEntrant, minuteSortieEntrant = personneEntrante
    for index, personneDansSalle in enumerate(dansSalle):
        minuteSortieSortant = personneDansSalle[1]
        if minuteSortieSortant < minuteArriveeEntrant:
            personneSortant.append(index)
        elif min(minuteSortieSortant, minuteSortieEntrant) - minuteArriveeEntrant >= 15:
            result += 1
    for idPersonne in personneSortant[::-1]:
        del dansSalle[idPersonne]
    dansSalle.append(personneEntrante)
"""

execution_time = timeit.timeit(aTester, number=1000)

print(f"Temps d'exécution moyen : {execution_time} secondes")