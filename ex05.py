# Definição da estrutura do nó
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Função que encontra o menor valor numa ABB
def menor_valor(node):
    if node is None:
        return None # árvore vazia
    
    atual = node
    while atual.left is not None:
        atual = atual.left

    return atual.value

# Construção da árvore
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right = Node(14)

# Teste
print("Menor valor:", menor_valor(root))
