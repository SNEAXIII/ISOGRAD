result = ""
lStatue, hStatue, lSalle, hSalle = map(int, input().split(" "))


def multiIntersect(y):
    intersect = linesDyna[y]
    for line in linesDyna[y + 1:y + 1 + hStatue]:
        intersect &= line
        if not intersect:
            return False
    return intersect.pop()


def fillGrid(x, y):
    for index in range(hStatue):
        copyLines = lines[y+index+1]
        lines[y+index+1] = copyLines[:x] + "x" * lStatue + copyLines[x+lStatue:]


def findLocation():
    for y in range(hSalle - hStatue):
        location = multiIntersect(y)
        if location:
            fillGrid(location, y)
            break


lines = [input() for _ in range(hSalle)]
linesDyna = []
for y, yElem in enumerate(lines):
    # print("______________________")
    count = 0
    linesDyna.append(set())
    for x, xElem in enumerate(yElem):
        if xElem == ".":
            count += 1
        elif xElem == "#":
            count = 0
        if count >= lStatue + 2:
            xGood = x - lStatue
            linesDyna[y].add(xGood)
            # print(xGood)

findLocation()

# print("____________________________________________")
# colonnesDyna = []
# print("les collones")
# for x in range(lSalle):
#     print("______________________")
#
#     count = 0
#     colonnesDyna.append(set())
#     for y in range(hSalle):
#         case = lines[y][x]
#         if case == ".":
#             count += 1
#         elif case == "#":
#             count = 0
#         if count >= hStatue + 2:
#             yGood = y - hStatue
#             colonnesDyna[x].add(yGood)
#             print(yGood)

for line in lines:
    print(line)

# print(f"lignes : {linesDyna}")
# print(f"colonnes : {colonnesDyna}")


# print(result)
