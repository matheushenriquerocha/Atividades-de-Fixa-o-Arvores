class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_ordem(node):
    if node is None:
        return []
    return [node.value] + pre_ordem(node.left) + pre_ordem(node.right)

def em_ordem(node):
    if node is None:
        return []
    return em_ordem(node.left) + [node.value] + em_ordem(node.right)

def pos_ordem(node):
    if node is None:
        return []
    return pos_ordem(node.left) + pos_ordem(node.right) + [node.value]

if __name__ == "__main__":
    raiz = Node(33)
    raiz.left = Node(15)
    raiz.right = Node(41)

    raiz.right.left = Node(38)
    raiz.right.left.left = Node(34)
    raiz.right.left.right = Node(43)

    raiz.right.right = Node(47)
    raiz.right.right.right = Node(49)

    print("Pré-ordem:")
    print(pre_ordem(raiz))

    print("Em-ordem:")
    print(em_ordem(raiz))

    print("Pós-ordem:")
    print(pos_ordem(raiz))
