# Given a binary tree, design an algorithm which create a 
# linked list of all nodes at each depth, if you have depth D, 
# there will be D linked lists.

class LLNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

def get_nodes_at_depth(node, depth, arr):
    if not node:
        return arr
    # import pdb; pdb.set_trace()
    if len(arr) <= depth:
        arr.append(LLNode(node.data))
    else:
        new_node = LLNode(node.data)
        arr[depth].next = new_node
    arr = get_nodes_at_depth(node.left, depth+1, arr)
    arr = get_nodes_at_depth(node.right, depth+1, arr)
    return arr

if __name__ == '__main__':
    child_node1 = TreeNode(9)
    child_node1.left = TreeNode(7)
    child_node1.right = TreeNode(6)
    child_node2 = TreeNode(5)
    child_node2.left = TreeNode(4)
    child_node2.right = TreeNode(3)
    root = TreeNode(10)
    root.left = child_node1
    root.right = child_node2

    # list of linked lists
    arr = []
    print(get_nodes_at_depth(root, 0, arr))
    
