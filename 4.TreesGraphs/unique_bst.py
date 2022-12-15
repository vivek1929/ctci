# Given an integer n, return the number of structurally unique BST's
#  (binary search trees) which has exactly n nodes of unique values from 1 to n.
# 95 leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # left included, right not included
        def helper(left, right) -> List[Optional[TreeNode]]: 
            if left == right - 1:
                return [TreeNode(left)]
            elif left > right - 1:
                return [None]
            else:
                list_of_trees = []
                for number in range(left, right):
                    for left_node in helper(left, number):
                        for right_node in helper(number + 1, right):
                            root = TreeNode(number)
                            root.left = left_node
                            root.right = right_node  
                            list_of_trees.append(root)
                return list_of_trees
        
        return helper(1, n+1) 