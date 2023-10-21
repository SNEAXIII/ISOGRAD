with open("input2.txt", "r", encoding="utf-8") as f:
    lines = [elem.split(" ") for elem in f.read().split("\n")]

maxi = int(lines[0][0]) - 2
dicto = {}

for line in lines[1:]:
    dicto[line[0]] = dicto.get(line[0], 0) + 1
    if dicto.get(line[0], 0) == maxi:
        for _line in lines[1:]:
            if _line[1] == line[0]:
                print(_line[0])
                break
        break
