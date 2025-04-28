class Node:
    def __init__ (self, data) :
        self.left = None
        self.right = None
        self.val = data

def in_order_traversal(root):
    if root :
        in_order_traversal(root.left)
        print(root.val, end="")
        in_order_traversal(root.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal:")
in_order_traversal(root)