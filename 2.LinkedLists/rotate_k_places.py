# Given the head of a linked list, rotate the list to the right by k places
# 61 of leetcode.

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if not head or not head.next:
            return head
        size = 0
        node = head
        while (node):
            size += 1
            node = node.next
        if k > size:
            k = k % size
        curr = head
        while (k > 0):
            curr = self.rotateOnceRight(curr)
            k -= 1
        return curr
    
    def rotateOnceRight(self, head):
        last = head
        prev = head
        while(last.next):
            prev = last
            last = last.next
        prev.next = None
        last.next = head
        return last