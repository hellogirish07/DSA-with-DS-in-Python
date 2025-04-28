class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node  # Corrected here

    def insert_after(self, prev_node, new_data):
        if not prev_node:
            print("The given previous node must be in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Creating a Linked List
linked_list = LinkedList()

# Adding initial values
linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)

# Performing operations
print("Inserting 5 at the beginning of the list")
linked_list.insert_begin(5)
linked_list.print_list()

print("Inserting 10 after 5")
linked_list.insert_after(linked_list.head.next, 10)
linked_list.print_list()

print("Inserting 15 at the end of the list")
linked_list.insert_end(15)
linked_list.print_list()
