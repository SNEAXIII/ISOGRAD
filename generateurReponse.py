with open("template.py","r",encoding="utf-8") as input:
    with open("responseToPaste.py","w",encoding="utf-8") as output:
        rawData = input.readlines()
        data = rawData[rawData.index("# START\n")+1:rawData.index("# END\n")]
        output.writelines(line for line in data)

# TODO importer les I/O