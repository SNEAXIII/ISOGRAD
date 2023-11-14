import shutil
for fileToOpen in ("moi", "gagnant"):
    with open(f"testVitesse/{fileToOpen}.py", "r", encoding="utf-8") as input:
        with open(f"testVitesse/autogeneratedTest{fileToOpen}.py", "w", encoding="utf-8") as output:
            with open("partialInput.py", "r", encoding="utf-8") as partial:
                rawData = input.read()
                data = "import timeit\naTester = \"\"\"\n" + \
                       partial.read() + rawData + \
                       "\"\"\"\nexecution_time = timeit.timeit(aTester, number=1000)\nprint(f\"Temps d\'exécution moyen : {execution_time} secondes\")"
                output.write(data)


dataSample = "1"

for fileType in ("input", "output"):
    shutil.copy2(f"dataSample/{fileType}{dataSample}.txt", "testVitesse")
