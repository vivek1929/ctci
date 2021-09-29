# Write a code to partition a linked list around a given value x, 
# such that all nodes less than x should combe before nodes that 
# are equal or greater than x. Partion can be anywhere. 
# E.g: input 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 (Partition around 5)
# output 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linkedlistnode import LinkedListNode

# Start a new list using existing nodes, elements bigger than pivot are put at 
# tail while smaller are put at head. 
def partition_linked_list(node, partition):
    head = node
    tail = node

    while (node != None):
        next = node.next
        if (node.data < partition):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head


if __name__ == '__main__':
    # Prepare input linked list
    input_ll = LinkedListNode(3)
    for each in [5, 8, 5, 10, 2, 1]:
        input_ll.appendnext(each)

    out_ll = partition_linked_list(input_ll, 5)

    # Print output linked list
    while (out_ll.next != None):
        print(out_ll.data)
        out_ll = out_ll.next
    print(out_ll.data)