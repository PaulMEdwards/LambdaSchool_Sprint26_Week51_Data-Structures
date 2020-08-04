"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
   Done
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
   Done
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   LinkedList manages it's own size and has different methods/properties from array.
"""

cur_dir = 'stack'
import sys, pathlib
if str(pathlib.Path.cwd()).endswith(cur_dir):
    sys.path.insert(0, str(pathlib.Path.cwd().parent))
if str(sys.path[0]).endswith(cur_dir):
    sys.path.insert(0, str(pathlib.Path.cwd()))

try: from singly_linked_list.singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass
try: from singly_linked_list import LinkedList
except ModuleNotFoundError: pass
except ImportError: pass

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if self.storage.length == 0: return None
        return self.storage.remove_tail()
