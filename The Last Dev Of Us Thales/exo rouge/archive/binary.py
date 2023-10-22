class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node, level=0):
    if node is None:
        return

    print_tree(node.right, level + 1)
    print("    " * level + str(node.value))
    print_tree(node.left, level + 1)

# Création des nœuds de l'arbre
tree = []
nombreGene = 4
nombrePossibilite = 2**nombreGene-1
for i in range(nombrePossibilite):
    tree.append(Node(i))

# Construction de l'arbre en établissant les relations entre les nœuds
for i in range(1, len(tree)):
    parent_index = (i - 1) // 2
    if i % 2 == 0:
        tree[parent_index].left = tree[i]
    else:
        tree[parent_index].right = tree[i]

# Affichage de l'arbre
print_tree(tree[0])
print(bin(15))