class Node:
    def __init__ (self, data) :
        self.data = data
        self.next = None
    
class Queue:
    def __init__ (self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, itom):
        temp = Node(itom)
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
    
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
    
    def display(self):
        temp = self.front
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next
        print("None")

q = Queue()

print("Queue :")
q.EnQueue(1)
q.display()
q.EnQueue(2)
q.display()
q.EnQueue(3)
q.display()
q.EnQueue(4)
q.display()
q.EnQueue(5)
q.display()

print("\nQueue after deleting element :")
q.DeQueue()
q.display()
q.DeQueue()
q.display()
q.DeQueue()
q.display()
q.DeQueue()
q.display()
q.DeQueue()
q.display()