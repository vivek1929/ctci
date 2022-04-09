# Given two trees T1 and T2 where T1 is much bigger that T2. Create an 
# algorithm to determine if T2 is subtree of T1

def check_trees_are_equal(node1, node2):

    if not node1 and node2:
        return False
    if node1 and not node2:
        return False
    if not node1 and not node2:
        return True
    # Pre order traversal
    if node1.data != node2.data:
        return False
    left = check_trees_are_equal(node1.left, node2.left)
    right = check_trees_are_equal(node1.right, node2.right)

    return left and right

def check_subtree(t1, t2):

    subtree = check_trees_are_equal(t1, t2)
    if subtree:
        return True
    check_subtree(t1.left, t2)
    check_subtree(t1.right, t2)
    return False