from copy import deepcopy
class Graph:
    def __init__(self):
        self.all = dict()

    def add(self, rawData):
        _from, _to = rawData.split()
        if _from in self.all:
            self.all[_from].add(_to)
        else:
            self.createNode(_from)

    def createNode(self, _from):
        self.all[_from] = Node()

    def parcours(self):
        max = 0
        result = 0
        for node in self.all:
            counter = 0
            aVisiter = deepcopy(self.all[node].next)
            while aVisiter:
                enCours = aVisiter.pop()
                aVisiter |= deepcopy(self.all[enCours].next)
                if self.all[enCours].type == 0:
                    counter+=1
            if max < counter:
                max = counter
                result = node
        return result


class Node:
    def __init__(self, elem=None):
        # 0 = house, 1 = protection
        self.type = 0
        self.next = set()
        if elem is not None:
            self.add(elem)

    def add(self, other):
        self.next.add(other)
        self.reset()

    def __len__(self):
        return len(self.next)

    def reset(self):
        _len = len(self)
        if _len != 0:
            self.type = 1

    def __str__(self):
        return f"{self.next}"


numberOfRelation, numberOfModule = map(int, input().split())

village = Graph()

for number in range(numberOfModule):
    village.createNode(str(number))
for _ in range(numberOfRelation):
    village.add(input())

result = village.parcours()
print(result)

