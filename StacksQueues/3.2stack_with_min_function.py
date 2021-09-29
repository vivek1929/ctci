# Stack apart from having push and pop, implement min function
# that returns minimum element. Push, pop and min should all 
# operate in O(1) time

import sys

# Calculating min on each push will take O(1). But for pop, if min
# is removed it takes O(n). But insteach min on each pop state is 
# same as one during the previous push state. So store min state
# during each push. So min will always take O(1) as pop and push do.
class Node:
    def __init__(self, value, min):
        self.value = value
        self.next = None
        self.min = min

class Stack:
	
    # The min values will be
    def __init__(self):
        self.head = Node("head", sys.maxsize)
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    # Get the current size of the stack
    def getSize(self):
        return self.size
        
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
        
    # Get the top item of the stack
    def peek(self):
        
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
    
    def min(self):
        if self.isEmpty():
            return sys.maxsize #x Error value
        return self.head.next.min

    # Push a value into the stack.
    def push(self, value):
        if self.head.next:
            min = value if value < self.head.next.min else self.head.next.min
        else:
            min = value if value < self.head.min else self.head.min
        # min = value if value < self.head.min else self.head.min
        node = Node(value, min)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    print(stack.min())