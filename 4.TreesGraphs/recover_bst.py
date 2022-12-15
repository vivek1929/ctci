# You are given the root of a binary search tree (BST), where the values of 
# exactly two nodes of the tree were swapped by mistake. Recover the tree 
# without changing its structure.
# 99 of leetcode

# Do inorder traversal, sort the output, then find and replace swapped nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tlist = []
        inOrder(root, tlist)
        tlist.sort()
        
        self.findAndReplace(root, tlist)
        return root
        
    def findAndReplace(self, root, tlist):

        if not root:
            return
        self.findAndReplace(root.left, tlist)
        if tlist[self.i] != root.val:
            root.val = tlist[self.i]
        self.i += 1
        self.findAndReplace(root.right, tlist)

def inOrder(tree, tlist):
    if not tree:
        return
    inOrder(tree.left, tlist)
    tlist.append(tree.val)
    inOrder(tree.right, tlist)

