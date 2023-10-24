import timeit
aTester = """
import sys, io

sampleToTest = "4"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
"""
execution_time = timeit.timeit(aTester, number=1000)
print(f"Temps d'exécution moyen : {execution_time} secondes")