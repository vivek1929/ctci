# Given a list of projects and its dependencies, all of the project dependencies
# should be build before the project is. Find a build order for projects to build
# If not an order, return an error. 
# E.g: Input = a, b, c, d, e, f 
# Dependencies = (a, d), (f, b), (b, d), (f, a), (d, c)'

# We can do depth first search by starting from arbitrary node and write dependency. 
# if we hit the end and haven't coverted some nodes, start dfs from that node again
# since that we have few dependencies already built, add any new nodes at beginning.
# Do this until we found all nodes. If there is any circular dependency, throw error.

class GraphNode:

    def __init__(self, data) -> None:
        self.data = data
        self.edges = set()
        self.state = 'UNVISITED'
    
    def add_edge(self, node):
        self.edges.add(node)


class Graph:

    def __init__(self) -> None:
        self.graph_dict = {}
    
    def get_or_create_node(self, data):
        if data not in self.graph_dict:
            node = GraphNode(data)
            self.graph_dict[data] = node
        return self.graph_dict[data]
    
    def add_edge(self, begin, end):
        self.get_or_create_node(begin)
        self.graph_dict[begin].\
            add_edge(self.get_or_create_node(end))

def get_dfs_path(node, path = []):
    if not node:
        return path
    path = [node.data]
    for each in node.edges:
        if each.state != 'VISITED':
            if each.state == 'VISITING':
                # Circular dependency error
                raise Exception('Cannot build dependency order')
            node.state = 'VISITING'
            path = path + get_dfs_path(each, path)
    node.state = 'VISITED'
    return path


if __name__ == '__main__':
    # set function only takes list else use {'a', 'b'..}
    projects = set(['a', 'b', 'c', 'd', 'e', 'f'])
    dependencies = Graph()
    dependencies.add_edge('a','d')
    dependencies.add_edge('f','b')
    dependencies.add_edge('b','d')
    dependencies.add_edge('f','a')
    dependencies.add_edge('d','c')

    path = []
    for each in projects:
        if each not in path:
            path = get_dfs_path(dependencies.get_or_create_node(each)) + path
    # Reverse to print build order
    print(path[::-1])