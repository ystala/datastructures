class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
    
    def enqueue(self, item):
        if self.rear == self.capacity - 1:
            raise OverflowError("Queue is full")
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.front == -1:
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front += 1
        return item
    
    def is_empty(self):
        return self.front == -1
