# Building a Queue Data Type
from collections import deque # Representing FIFO and LIFO Queues with a Deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
        
# Building a Stack Data Type
class Stack(Queue): # Extending Queue class using inheritance
    def dequeue(self): # Overriding the .dequeue method
        return self._elements.pop()

# Building a PriorityQueue Data Type