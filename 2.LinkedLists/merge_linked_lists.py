# You are given an array of k linked-lists lists, each linked-list is 
# sorted in ascending order. Merge all the linked-lists into one sorted 
# linked-list and return it.

import copy
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n < 1:
            return None
        if n == 1:
            return lists[0]
        final_node = lists.pop(0)
        for i in range(len(lists)):
            final_node = self.mergeTwoNodes(final_node, lists[i])
        return final_node

    def mergeTwoNodes(self, node1, node2):
        head = node1
        while(node1 != None and node2 != None):
            if node1.val > node2.val:
                newnode = copy.deepcopy(node1)
                node1.val = node2.val
                node1.next = newnode
                node2 = node2.next
                node1 = node1.next
            else:
                node1 = node1.next

        if(node2):
            tempnode = head
            if tempnode == None:
                head = node2
            else:
                while(tempnode.next != None):
                    tempnode = tempnode.next
                tempnode.next = node2
        return head