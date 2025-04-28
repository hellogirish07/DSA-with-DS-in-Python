class Stack:
    def __init__(self, size) :
        self.array = [None] * size
        self.capacity = size
        self.top = -1

    # Push operation
    def push(self, val) :
        if self.isFull() :
            print("Stack is full")
            exit(-1)
        print("Insteting element into the stack :", val)
        self.top = self.top + 1
        self.array[self.top] = val
    
    # Pop operation
    def pop(self) :
        if self.isEmpty() :
            print("Stack is empty")
            exit(-1)
        print("Deleting element from the stack is : ", self.peek()) 
        val = self.array[self.top]
        self.top = self.top - 1
        return val
    
    # peak operation
    def peek(self) :
        if self.isEmpty() :
            print("Stack is empty")
            exit(-1)
        return self.array[self.top]
    
    # size operation
    def size(self) :
        return self.top + 1
    
    def isEmpty(self) :
        return self.size() == 0
    
    def isFull(self) :
        return self.capacity == self.size()
    
# Driver code
stack = Stack(5)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print("Stack : ", stack.array)
print("Stack size is : ", stack.size())
print("Top element is : ", stack.peek())

stack.pop()
stack.pop()
stack.pop()
print("Stack size is : ", stack.size())
print("Top element is : ", stack.peek())