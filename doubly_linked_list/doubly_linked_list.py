"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def printAllValues(self, label = None):
        if label: print(label)
        n = self.head
        i = 0
        while n is not None:
            print(f"#{i}\t{n.value}\t{n}")
            i += 1
            n = n.next

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # self.printAllValues("BEGIN add_to_head")
        # print(f"value to add\t{value}")

        node = ListNode(value, None, self.head)
        if self.length == 0:
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
        self.head = node
        self.length += 1

        # self.printAllValues("END add_to_head")

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # self.printAllValues("BEGIN remove_from_head")

        if self.head is not None:
            v = self.head.value
            if self.length == 1:
                self.tail = None
                self.head = None
            elif self.head.next is not None:
                self.head.next.prev = None
            self.length -= 1
            return v

        # self.printAllValues("END remove_from_head")

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # self.printAllValues("BEGIN add_to_tail")
        # print(f"value to add\t{value}")

        node = ListNode(value, self.tail, None)
        if self.length == 0:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.length += 1

        # self.printAllValues("END add_to_tail")

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # self.printAllValues("BEGIN remove_from_tail")

        if self.tail is not None:
            v = self.tail.value
            if self.length == 1:
                self.tail = None
                self.head = None
            elif self.tail.prev is not None:
                self.tail.prev.next = None
            self.length -= 1
            return v

        # self.printAllValues("END remove_from_tail")

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # self.printAllValues("BEGIN move_to_front")
        # print(f"node to move\t{node}")

        # Already at beginning
        if node == self.head:
            # print("already at beginning")
            pass
        # At end
        elif node == self.tail:
            # print("moving self.tail to self.head")
            self.tail = self.tail.prev
            self.tail.next = None
        # somewhere in the middle
        else:
            # print("moving from middle")
            node.next.prev = node.prev
            node.prev.next = node.next
        # common
        node.prev = None
        node.next = self.head
        self.head = node

        # self.printAllValues("END move_to_front")

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # self.printAllValues("BEGIN move_to_end")
        # print(f"node to move\t{node}")

        # Already at end
        if node == self.tail:
            pass
        # At beginning
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
            self.head.next = node
        # somewhere in the middle
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
        # common
        node.next = None
        node.prev = self.tail
        self.tail = node

        # self.printAllValues("END move_to_end")

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # self.printAllValues("BEGIN delete")
        # print(f"node to delete\t{node}")

        if self.length == 1:
            self.tail = self.head = node.tail = node.head = None
        else:
            if node == self.head:
                self.head = node.next
                node.next.prev = None
            elif node == self.tail:
                self.tail = node.prev
                node.prev.next = None
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
        self.length -= 1

        # self.printAllValues("END delete")

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # print("BEGIN get_max")
        # self.printAllValues("get_max")

        # iterate through all elements
        i = 0
        max = -1
        n = self.head
        while n is not None:
            v = n.value
            # print(f"#{i}\t{v}\t{n}")
            # print(f"\t\t({v} > {max} = {v>max})")
            if v > max:
                max = v
            n = n.next
            i += 1

        # print("END get_max")
        # print(f"max = {max}")

        return None if max == -1 else max
