# Implement algorithm to delete a node in the middle. 

from linkedlistnode import LinkedListNode

# Here we don't have access for entire node, only the node to be deleted
# So solution is to copy data from next node to current node.
def delete_node(node):
    if (node.next == None):
        return False
    next = node.next
    node.data = next.data
    node.next = next.next
    return True

if __name__ == '__main__':
    # Prepare FOLLOW UP linked list
    input_ll = LinkedListNode('F')
    for each in 'OLLOW UP':
        input_ll.appendnext(each)
    
    
