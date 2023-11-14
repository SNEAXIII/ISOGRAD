import timeit
aTester = """
import sys, io

sampleToTest = "1"
with open(f"output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    sys.stdin = io.StringIO(f.read())
s1, s2 = input(), input()
common_elements = set(s1) & set(s2)
order1 = ''.join(c for c in s1 if c in common_elements)
order2 = ''.join(c for c in s2 if c in common_elements)
if order1 != '' and order1 == order2:
    print('TEMPETE')
    print(order1)
else:
    print('NORMAL')

"""
execution_time = timeit.timeit(aTester, number=10000)
print(f"Temps d'exécution moyen : {execution_time} secondes")