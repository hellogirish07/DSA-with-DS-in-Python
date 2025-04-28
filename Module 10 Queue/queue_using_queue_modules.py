from queue import Queue
q = Queue(maxsize=5)

q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)

print("Queue :", q.queue)
print("Removed Element :" ,q.get())
print("Queue :", q.queue)