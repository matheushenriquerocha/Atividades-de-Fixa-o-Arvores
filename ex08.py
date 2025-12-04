# Estrutura do nó
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Função para calcular a altura da árvore
def altura(node):
    if node is None:
        return -1
    return 1 + max(altura(node.left), altura(node.right))

# Criação da ABB
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.right.left = Node(12)
root.right.right = Node(18)

# Teste
print("Altura da árvore:", altura(root))