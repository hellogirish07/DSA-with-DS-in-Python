# Sum of Element in Binary Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_bt(root) :
    if root == None:
        return 0
    return (root.data + add_bt(root.left) + add_bt(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

sum = add_bt(root)

print("Sum of the all node of the BT is :", sum)