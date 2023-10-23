import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

line1 = lines[0].replace("\n","").split(" ")
line2 = lines[1].split(" ")
duree1 = int(line1[1]) * (int(line1[2]) + int(line1[3]))
duree2 = int(line2[1]) * (int(line2[2]) + int(line2[3]))

if duree1 < duree2:
    print(line1[0])
else:
    print(line2[0])