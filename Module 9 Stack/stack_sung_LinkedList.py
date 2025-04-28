class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None   

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None 
            return popped.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    
    def display(self):
        internode = self.head
        if self.isEmpty():
            print("Stack Underflow")
        else:
            while(internode != None):
                print(internode.data, end=" ")
                internode = internode.next
                if (internode != None):
                    print("->", end=" ")
            return

MyStack = Stack()
MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)
MyStack.push(55)

print("Top Element :", MyStack.peek())
print("Stack :")
MyStack.display()

MyStack.pop()
MyStack.pop()
MyStack.pop()
print("\n")
print("Stack after Pop :")
MyStack.display()
