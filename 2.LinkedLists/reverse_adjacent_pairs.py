# Given a linked list, swap every two adjacent nodes and return its head. 
# You must solve the problem without modifying the values in the list's nodes 
#   (i.e., only nodes themselves may be changed.)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next == None:
            return head
        node1 = head
        node2 = head.next
        
        node1.next = self.swapPairs(node2.next)
        node2.next = node1
        
        return node2