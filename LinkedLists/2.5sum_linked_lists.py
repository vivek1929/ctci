# We have two numbers represented by linked lists in reverse order i.e., 
# number 246 is represented as 6 -> 4 -> 2. Write a function to sum 
# both lists and written result as a new linked list. 
# E.g: 7 -> 1 -> 6 + 5 -> 9 -> 2 ==> 617 + 295 = 912 is 2 -> 1 -> 9

from linkedlistnode import LinkedListNode

def sum_reverse_linked_lists(a, b):
    pass

if __name__ == '__main__':
    a = LinkedListNode(7)
    for each in [1, 6]:
        a.appendnext(each)
    
    b = LinkedListNode(5)
    for each in [9, 2]:
        b.appendnext(each)