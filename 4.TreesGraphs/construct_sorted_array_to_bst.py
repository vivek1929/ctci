# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the 
# two subtrees of every node never differs by more than one.
# 108 leetcode 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = buildBalancedSubtree(nums)
        return root

def buildBalancedSubtree(nums):
    if not nums:
        return None
    mid = nums[len(nums)//2]
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2+1:]
    root = TreeNode(mid)
    root.left = buildBalancedSubtree(left)
    root.right = buildBalancedSubtree(right)
    return root

# Given the head of a singly linked list where elements are sorted in 
# ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a 
# binary tree in which the depth of the two subtrees of every node 
# never differ by more than 1.
# 109 leetcode