# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    rev = None
    while (head):
        temp = ListNode(head.val)
        temp.next = rev
        rev = temp
        head = head.next
    return rev