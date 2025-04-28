class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def search(self, key):
        if self.key == key:
            return self
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        return None

    def print_inorder(self):
        if self.left:
            self.left.print_inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.print_inorder()

    def print_preorder(self):
        print(self.key, end=" ")
        if self.left:
            self.left.print_preorder()
        if self.right:
            self.right.print_preorder()

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.key, end=" ")

# Creating the BST
root = Node(43)
root.insert(10)
root.insert(79)
root.insert(90)
root.insert(12)
root.insert(54)

# Searching for a value
result = root.search(90)
if result:
    print("Found:", result.key)
else:
    print("Not found")

print("BST in Inorder :")
root.print_inorder()

print("\nBST in Postordder :")
root.print_postorder()

print("\nBST in Preorder :")
root.print_preorder()
