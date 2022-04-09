

class Tree:

    def __init__(self, node) -> None:
        self.root = node
    
    def in_order_traversal(self, root):
        result = []
        if root:
            result = self.in_order_traversal(root.left)
            result.append(root.data)
            result = result + self.in_order_traversal(root.right)
        return result

class Node:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)

    myTree = Tree(root)
    print(myTree.in_order_traversal(root))