from collections import deque

q = deque()

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print("Deque :",q)

print("Element Deleted from Deque :", q.pop()) # Remove element from Right 
print("Element Deleted from Deque :", q.popleft()) # Remove element from Left
print("Deque :",q)
