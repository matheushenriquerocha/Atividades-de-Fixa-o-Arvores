class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def pre_ordem(self, node):
        if node is None:
            return []
        return [node.value] + self.pre_ordem(node.left) + self.pre_ordem(node.right)
    
    def em_ordem(self, node):
        if node is None:
            return []
        return self.em_ordem(node.left) + [node.value] + self.em_ordem(node.right)
    
    def pos_ordem(self, node):
        if node is None:
            return []
        return self.pos_ordem(node.left) + self.pos_ordem(node.right) + [node.value]
    
tree = BST()
valores = [7, 8, 3, 4, 2, 1, 6, 5]

for v in valores:
    tree.insert(v)

print("Pré-ordem:", tree.pre_ordem(tree.root))
print("Em-ordem:", tree.em_ordem(tree.root))
print("Pós-ordem:", tree.pos_ordem(tree.root))
