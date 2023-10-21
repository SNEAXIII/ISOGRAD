sampleToTest = "1"
with open(f"dataSample/output{sampleToTest}.txt") as f:
    outputExpected = f.read()
with open(f"dataSample/input{sampleToTest}.txt", "r", encoding="utf-8") as f:
    inputGiven = (f.readlines()[1].rstrip("\n")).split(" ")
with open("gneu","w",encoding="utf-8") as f:
    for gene in inputGiven:
        f.write(f"{gene}\n{gene[::-1]}\n{outputExpected}\n")
