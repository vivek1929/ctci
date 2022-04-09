# Implement MyQueue class using two stacks.

# Difference in Stack and Queue is its order. For all pop and peek operations
# need to reverse order. Reverse can be done by continuous pop and push to 
# other stack. This can be optimized to perform lazy pop and peek only when 
# necessary. So use two stacks one for storing is stack order and other for queue
# order where pop and peek are performed. Only copy to queue order stack if necessary.


from stack_implementation import Stack

class MyQueue:

    def __init__(self) -> None:
        self.stack_order = Stack()
        self.queue_order = Stack()

    def enqueue(self, value):
        self.stack_order.push(value)
    
    def dequeue(self, value):
        self.shift_stacks()
        self.queue_order.pop()
    
    def shift_stacks(self):
        # Only do shifting if empty, hence a lazy shift.
        if (self.queue_order.isEmpty()):
            while(not self.stack_order.isEmpty()):
                self.queue_order.push(self.stack_order.pop())
