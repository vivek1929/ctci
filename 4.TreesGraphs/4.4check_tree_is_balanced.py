# Implement a function to check if a binary tree is balanced. A balaced tree
# is defined to be a tree such that the height of two subtrees of any node 
# never differ by more than one.

def get_tree_height(node):
    if not node:
        return 0
    height = max(get_tree_height(node.left), get_tree_height(node.right)) + 1
    return height
    

def is_tree_balanced(node):
    if not node:
        return True

    left_height = get_tree_height(node.left)
    right_height =  get_tree_height(node.right)

    if abs(left_height -right_height) > 1:
        return False
    else:
        return is_tree_balanced(node.left) and is_tree_balanced(node.right)