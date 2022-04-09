# Linked list is a ds that represents sequence of nodes. In singly linked list
# each points to next node in sequence. While double linked list points to previous
# and next record in sequence. 
# A linked list doesn't provide constant time access to kth element. 
# Benefits of linked list is that you can add or remove items from beginning of
# list in constant time.

class LinkedListNode:

    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    # Not providing constant time for add or remove.
    # TODO Store tail as well to provide constant time
    # for add and remove
    def appendnext(self, data):
        tail = LinkedListNode(data)
        n = self
        while (n.next != None):
            n = n.next
        n.next = tail

# Deleting a node is updating next element to .
def deletenode(head, data):
    n = head
    if (head.data == data):
        # Moving head to next, hence deleted head
        return head.next

    while (n.next != None):
        if (n.next.data == data):
            n.next = n.next.next
            return head
        n = n.next
    return head

if __name__ == '__main__':
    a = LinkedListNode('a')
    a.appendnext('b')
    print (a.next.data)
    deletenode(a, 'b')
    print(a.next)
