# Given the roots of two binary trees p and q, write a function to 
# check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.
# 100 leetcode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q or p and not q:
            return False
        if not p and not q:
            return True
        if not self.isSameTree(p.left, q.left):
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p.right, q.right):
            return False
        return True