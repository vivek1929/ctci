# Write a code to remove duplicates from unsorted linked list


from linkedlistnode import LinkedListNode

def remove_duplicates(ll):
    head = ll
    unique_chars =set()
    while (ll.next != None):
        if ll.data not in unique_chars:
            unique_chars.add(ll.data)
            previous = ll
        else:
            previous.next = ll.next
        ll = ll.next
    return head

if __name__ == '__main__':
    # Prepare FOLLOW UP linked list
    input_ll = LinkedListNode('F')
    for each in 'OLLOW UP':
        input_ll.appendnext(each)
    
    out_ll = remove_duplicates(input_ll)
    while (out_ll.next != None):
        print(out_ll.data)
        out_ll = out_ll.next
    print(out_ll.data)