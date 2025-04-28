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

    def find_min(self):
        # Helper function to find the minimum value node in the right subtree
        current = self
        while current.left:
            current = current.left
        return current

    def delete(self, key):
        # Function to delete a node from the BST
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.delete(key)
        else:
            # Case 1: No child
            if not self.left and not self.right:
                return None  # Simply remove the node
            
            # Case 2: One child
            if not self.left:
                return self.right  # Replace node with right child
            if not self.right:
                return self.left  # Replace node with left child

            # Case 3: Two children
            min_larger_node = self.right.find_min()  # Find inorder successor
            self.key = min_larger_node.key  # Copy inorder successor value
            self.right = self.right.delete(min_larger_node.key)  # Delete inorder successor
        
        return self 

    def print_inorder(self):
        # Print BST in sorted order (Left → Root → Right)
        if self.left:
            self.left.print_inorder()
        print(self.key, end=" ")
        if self.right:
            self.right.print_inorder()

# Creating the BST
root = Node(43)
root.insert(10)
root.insert(79)
root.insert(90)
root.insert(12)
root.insert(54)

# Printing before deletion
print("BST before deletion:")
root.print_inorder()

# Deleting a node
key_to_delete = 79
print(f"\nDeleting node {key_to_delete}...\n")
root = root.delete(key_to_delete)

# Printing after deletion
print("BST after deletion:")
root.print_inorder()
