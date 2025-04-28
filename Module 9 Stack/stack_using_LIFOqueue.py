from queue import LifoQueue

stack = LifoQueue(maxsize = 5)
print(stack.qsize())

stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)

print("Stack size is : ", stack.qsize())    
print("Stack : ", stack.queue)
print("Top element is : ", stack.queue[-1])

print("Element Popped from the stack :")
print("Deleting element from the stack is : ",stack.get())
print("Deleting element from the stack is : ",stack.get())
print("Deleting element from the stack is : ",stack.get())
print("Stack :", stack.queue)
