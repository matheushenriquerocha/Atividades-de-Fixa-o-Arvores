# Estrutura do nó
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Função que soma todos os valores da árvore
def soma_arvore(node):
    if node is None:
        return 0
    return node.value + soma_arvore(node.left) + soma_arvore(node.right)

# Criação de uma árvore binária
root = Node(15)
root.left = Node(7)
root.right = Node(20)
root.left.left = Node(3)
root.left.right = Node(9)
root.right.right = Node(25)

# Teste
print("Soma total da árvore:", soma_arvore(root))
