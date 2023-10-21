import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n').split(" "))

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
