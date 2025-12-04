# Estrutura do nó
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Função para encontrar o maior valor em uma ABB
def maior_valor(node):
    if node is None:
        return None
    
    atual = node
    while atual.right is not None:
        atual = atual.right

    return atual.value

# Construção da ABB
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Teste
print("Maior valor:", maior_valor(root))
