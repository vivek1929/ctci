# Given two integer arrays preorder and inorder where 
# preorder is the preorder traversal of a binary tree and 
# inorder is the inorder traversal of the same tree, 
# construct and return the binary tree.
# 105 leetcode

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

# Given two integer arrays inorder and postorder where 
# inorder is the inorder traversal of a binary tree and 
# postorder is the postorder traversal of the same tree, 
# construct and return the binary tree.
# 106 leetcode

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
