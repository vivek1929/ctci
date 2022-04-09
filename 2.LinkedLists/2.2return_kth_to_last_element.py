# Written a algorithm to return kth to last element in a linked list. 
# If k = 1, return last element and if k = 2, return second to last element. 

# If we know length we can simply return length-k element. But here we assume
# that  lenght is not known. 
from linkedlistnode import LinkedListNode

def print_kth_to_last(head, k):
    if (head == None):
        return (0, None)
    # Index will return 0 to last next element and 1 to last element and so on.
    # Since python, we are returning both index and  node at once easily.
    index, node = print_kth_to_last(head.next, k)
    index = index + 1
    if (index == k):
        return index, head
    return index, node

if __name__ == '__main__':
    # Prepare FOLLOW UP linked list
    input_ll = LinkedListNode('F')
    for each in 'OLLOWUP':
        input_ll.appendnext(each)
    
    _, out = print_kth_to_last(input_ll, 2)
    print (out.data)