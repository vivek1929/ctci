# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.
# 104 leetcode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = self.findMaxDepth(root, 1, [])
        return max(depths)

    def findMaxDepth(self, root, cur, depths):
        if not root:
            depths.append(cur-1)
            return depths
        self.findMaxDepth(root.left, cur+1, depths)
        self.findMaxDepth(root.right, cur+1, depths)
        return depths