# Given the head of a sorted linked list, delete all nodes 
# that have duplicate numbers, leaving only distinct numbers 
# from the original list. Return the linked list sorted as well.
# 81, 82 leetcode

# Input =  1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
# Output = 1 -> 2 -> 3 -> 4 -> 5

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head;
    while curr:
        while curr.next and curr.next.val ==curr.val:
            curr.next = curr.next.next
        curr = curr.next

    return head

# Input =  1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
# Output = 1 -> 3 -> 5

def deleteAllDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # sentinel
    sentinel = ListNode(0, head)

    # predecessor = the last node 
    # before the sublist of duplicates
    pred = sentinel
    
    while head:
        # if it's a beginning of duplicates sublist 
        # skip all duplicates
        if head.next and head.val == head.next.val:
            # move till the end of duplicates sublist
            while head.next and head.val == head.next.val:
                head = head.next
            # skip all duplicates
            pred.next = head.next 
        # otherwise, move predecessor
        else:
            pred = pred.next 
            
        # move forward
        head = head.next
        
    return sentinel.next