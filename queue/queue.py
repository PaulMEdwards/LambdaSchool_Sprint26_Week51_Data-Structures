"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
   Done
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
   Done
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   Quite a few differences... LinkedList manages it's own size and has different methods/properties from array.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

cur_dir = 'queue'
import sys, pathlib
if str(pathlib.Path.cwd()).endswith(cur_dir):
    sys.path.insert(0, str(pathlib.Path.cwd().parent))
if str(sys.path[0]).endswith(cur_dir):
    sys.path.insert(0, str(pathlib.Path.cwd()))
sys.path.insert(0, str(pathlib.Path.cwd().parent))

try: from singly_linked_list.singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass
try: from singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass

class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        s = self.storage.length
        # print(f"Size: {s}")
        return s

    def enqueue(self, value):
        # print(f"Enqueue: {value}")
        self.storage.add_to_tail(value)
        # print(f"Size: {self.storage.length}")

    def dequeue(self):
        if self.storage.length == 0: return None
        # print(f"Value: {self.storage.head.get_value()}")
        v = self.storage.head.get_value()
        self.storage.remove_head()
        return v
