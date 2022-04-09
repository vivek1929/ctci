# In stack of plates, the stack might topple if too high. So implement SetOfStacks
# that create a new stack when stack reaches max height. The push and pop should work
# as a regular stack. 

class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None 

class Stack:

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # Get the current size of the stack
    def getSize(self):
        return self.size
        
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
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

class SetOfStacks:

    def __init__(self, size) -> None:
        self.stack_max_size = size
        self.stacks = [Stack()]
    
    def push(self, value):
        last_stack = self.stacks[:-1]
        if (last_stack.getSize() < self.stack_max_size):
            last_stack.push(value)
        else:
            new_stack = Stack()
            new_stack.push(value)
            self.stacks.append(new_stack)
    
    def pop(self):
        last_stack = self.stacks[:-1]
        value = last_stack.pop()
        if (last_stack.isEmpty()):
            self.stacks.pop()