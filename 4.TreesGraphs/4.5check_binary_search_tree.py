# Implement a function to check if a binary tree is a binary search tree. 
# For binary search tree all left <= root <= all right

import sys
from binary_tree_implementation import Node

def is_tree_bst(node, min = None, max = None):
    if not node:
        return True
    
    # For root, max and min are None and
    # for left, min is None and right max is none
    if (max and max < node.data) or (min and min > node.data):
        return False
    else:
        return is_tree_bst(node.left, min, node.data) \
                and is_tree_bst(node.right, node.data, max)


if __name__ == '__main__':
    root = Node(200)
    print(is_tree_bst(root))