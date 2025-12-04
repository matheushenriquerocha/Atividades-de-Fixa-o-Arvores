# Estrutura de Nó da Àrvore
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Funções do Percurso
def pre_ordem(node):
    if node:
        print(node.value, end=" ")
        pre_ordem(node.left)
        pre_ordem(node.right)

def em_ordem(node):
    if node:
        em_ordem(node.left)
        print(node.value, end=" ")
        em_ordem(node.right)

def pos_ordem(node):
    if node:
        pos_ordem(node.left)
        pos_ordem(node.right)
        print(node.value, end=" ")

# Construção da árvore conforme o enunciado
root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)

# Impressão dos percursos
print("Pré-ordem:")
pre_ordem(root)

print("\nEm-ordem:")
em_ordem(root)

print("\nPós-ordem:")
pos_ordem(root)
print()
