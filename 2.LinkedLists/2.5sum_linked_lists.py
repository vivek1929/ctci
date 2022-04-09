# We have two numbers represented by linked lists in reverse order i.e., 
# number 246 is represented as 6 -> 4 -> 2. Write a function to sum 
# both lists and written result as a new linked list. 
# E.g: 7 -> 1 -> 6 + 5 -> 9 -> 2 ==> 617 + 295 = 912 is 2 -> 1 -> 9

from linkedlistnode import LinkedListNode

def sum_reverse_linked_lists(a, b):
    sum = a.data*pow(10, 0)
    i = 1
    while (a.next != None):
        sum += a.next.data*pow(10, i)
        i = i + 1
        a = a.next
    sum += b.data*pow(10, 0)
    i = 1
    while (b.next != None):
        sum += b.next.data*pow(10, i)
        i = i + 1
        b = b.next
    op = None
    while (sum > 1):
        if not op:
            op = LinkedListNode(sum % 10)
        else:
            op.appendnext(sum % 10)
        sum = sum // 10
    return op
if __name__ == '__main__':
    a = LinkedListNode(7)
    for each in [1, 6]:
        a.appendnext(each)
    
    b = LinkedListNode(5)
    for each in [9, 2]:
        b.appendnext(each)
    out_ll = sum_reverse_linked_lists(a, b)
    while (out_ll.next != None):
        print(out_ll.data)
        out_ll = out_ll.next
    print(out_ll.data)