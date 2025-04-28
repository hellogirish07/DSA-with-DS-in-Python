class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def preorder_traversal(node):
    if node:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
preorder_traversal(root)