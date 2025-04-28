class Node:
    def __init__(self, data = None): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            currunt = self.head
            while currunt.next is not None:
                currunt = currunt.next
            currunt.next = new_node

    def find_max(self):
        if self.head is None:
            return None
        max_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

my_list = LinkedList()
my_list.add_node(1)
my_list.add_node(2)
my_list.add_node(3)

print(my_list.find_max())  # Output: 3