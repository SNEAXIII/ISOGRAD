sampleToMake = "Custom2"
with open(f"dataSample/output{sampleToMake}.txt","w") as f:
    f.write("ACGTTCGACAT")
with open(f"dataSample/input{sampleToMake}.txt", "w", encoding="utf-8") as f:
    aAjouter = "ACGTT GTTCGA TAC"
    f.write(f"{len(aAjouter.split(' '))}\n{aAjouter}")

