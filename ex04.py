class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def contar_folhas(node):
    # Se a árvore estiver vazia
    if node is None:
        return 0

    # Se o nó não possui filhos -> é folha
    if node.left is None and node.right is None:
        return 1

    # Soma as folhas da esquerda e direita
    return contar_folhas(node.left) + contar_folhas(node.right)

# Construindo a árvore
root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)

# Chamando a função
print("Quantidade de folhas:", contar_folhas(root))
