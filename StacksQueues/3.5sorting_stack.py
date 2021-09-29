# Write a program to sort a stack so that smallest items at the top. 
# You can use additional temporary stack but may not copy to other data structures

# We can solve this using Tower of Hanoi principle where we need to use temporary 
# stack to oder the original stack to new stack. But here we have only one other
# stack. So 
from stack_implementation import Stack

def sort(s):
    temp_stack = Stack()
    while (not s.isEmpty()):
        temp = s.pop()
        while((not temp_stack.isEmpty()) and temp_stack.peek() > temp):
            s.push(temp_stack.pop())
        temp_stack.push(temp)
    return temp_stack