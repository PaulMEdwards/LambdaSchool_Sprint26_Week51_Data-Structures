"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

DEPTH = [10]

def printUtil(node, gap):
    if (node is None):
        return
    gap += DEPTH[0]
    printUtil(node.right, gap)
    print()
    for i in range(DEPTH[0], gap):
        print(end = " ")
    print(f"{node.value} ({node.count})")
    printUtil(node.left, gap)
    print()

def printValues(node, label = None):
    if label: print(label)
    printUtil(node, 0)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

    # Insert the given value into the tree
    def insert(self, value):
        if value == self.value:
            self.count += 1
            # print(f"incremented count for value:\t{self.value} ({self.count})")
        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # printValues(self, f"inserted:\t{value}")

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target_value to cur_value
            # 1. == return True
            # 2. < go left
            # 3. > go right
            # 4. not found, return False
        result = False
        ripCord = False
        n = self
        while result != True and n is not None:
            if target == n.value: result = True
            elif target > n.value:
                if n.right is not None:
                    n = n.right
                else:
                    n = None
            elif target < n.value:
                if n.left is not None:
                    n = n.left
                else:
                    n = None
            else:
                n = None
        # printValues(self, f"contains {target}?\t{result}")
        return result

    # Return the maximum value found in the tree
    def get_max(self):
        # print("get_max")
        n = self
        while n is not None:
            max = n.value
            n = n.right
        # print(f"max = {max}")
        return max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        n = self
        # print(f"v: {n.value}\nl: {n.left}\nr: {n.right}\n")
        fn(n.value)
        if n.left is not None: n.left.for_each(fn)
        if n.right is not None: n.right.for_each(fn)

    # STRETCH
    def delete(self, value):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# # print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()
