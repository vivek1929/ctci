# Given a directed graph (uni-directional), design an algorithm to find whether
# there is a route between two nodes. 

from graph_implementation_using_dict import Graph

# Depth First Search where we are saving visited nodes in a list so that we 
# will not end up in infinite loop. 
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start==end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
            return None


if __name__ == '__main__':
    mygraph = Graph()
    mygraph.add_edge('1','2')
    mygraph.add_edge('1','3')
    mygraph.add_edge('2','3')
    mygraph.add_edge('2','1')
    mygraph.add_edge('3','1')
    mygraph.add_edge('3','2')
    mygraph.add_edge('3','4')
    mygraph.add_edge('4','3')

    print(find_path(mygraph.graph_dict, '2', '4'))
