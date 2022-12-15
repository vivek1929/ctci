# Given the root of a binary tree and an integer targetSum, 
# return true if the tree has a root-to-leaf path such that 
# adding up all the values along the path equals targetSum.
# A leaf is a node with no children.
# 112 of leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        curr = targetSum - root.val
		
		# if this is required end node of path
        if not root.left and not root.right and curr == 0:
            return True
            
        return self.hasPathSum(root.left,curr) or self.hasPathSum(root.right,curr)


# Given the root of a binary tree and an integer targetSum, 
# return all root-to-leaf paths where the sum of the node values 
# in the path equals targetSum. Each path should be returned as a 
# list of the node values, not node references.
# A root-to-leaf path is a path starting from the root and ending 
# at any leaf node. A leaf is a node with no children.
#113 of leetcode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        ans = findPath(root, targetSum, [], ans)
        return ans

def findPath(root, target, curr, ans):
    if not root:
        return
    if root.left == None and root.right == None:
        if target == root.val:
            curr = curr + [root.val]
            ans.append(curr)
        return ans
    target = target - root.val
    findPath(root.left, target, curr + [root.val], ans)
    findPath(root.right, target, curr + [root.val], ans)
    return ans

