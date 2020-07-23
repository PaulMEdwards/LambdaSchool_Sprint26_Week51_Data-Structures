"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
   Done
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        s = self.size
        print(f"Size: {s}")
        return s

    def enqueue(self, value):
        # print(f"Enqueue: {value}")
        self.storage.insert(0, value)
        self.size += 1
        # print(f"Size: {self.size}")

    def dequeue(self):
        i = self.size - 1
        # print(f"Dequeue: #{i}, len={self.size}")
        if i < 0: return None
        # print(f"Value: {self.storage[i]}")
        v = self.storage.pop(i)
        self.size -= 1
        return v
