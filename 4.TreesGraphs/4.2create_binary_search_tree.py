# Given a sorted(ascending) array with unique integer elements, write an
# algorithm to create a binary search tree with minimal height. 


from binary_tree_implementation import Tree, Node

def create_minimal_bst(arr, start, end):
    if end < start:
        return None
    mid = (start + end)//2
    root = Node(arr[mid])
    root.left = create_minimal_bst(arr, start, mid-1)
    root.right = create_minimal_bst(arr, mid+1, end)
    return root

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    root = create_minimal_bst(arr, 0, len(arr)-1)
    bst = Tree(root)