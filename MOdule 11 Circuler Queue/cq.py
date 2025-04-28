class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue (Insert element)
    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full! Cannot insert", data)
            return
        if self.front == -1:  # First element insertion
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"Inserted: {data}")

    # Dequeue (Remove element)
    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty! Cannot dequeue")
            return
        removed_element = self.queue[self.front]
        if self.front == self.rear:  # If only one element was present
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Removed: {removed_element}")

    # Display queue elements
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return
        print("Queue Elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

# Example usage
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()  # Show queue elements

cq.dequeue()
cq.display()

cq.enqueue(60)  # Insert after removal
cq.display()
