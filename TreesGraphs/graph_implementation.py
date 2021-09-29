# Adjacency list representation of the graph using dictionary(as most suggesting)
# https://medium.com/youstart-labs/implement-graphs-in-python-like-a-pro-63bc220b45a0


class Graph:

    def __init__(self) -> None:
        self.graph_dict = {}

    def add_edge(self, node, adjacent):
        if node not in self.graph_dict:
            self.graph_dict[node] = set(adjacent)
        else:
            self.graph_dict[node].add(adjacent)

    def show_edges(self):
        for node in self.graph_dict:
            for adjacent in self.graph_dict[node]:
                print(node + ' -> ' + adjacent)

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

    mygraph.show_edges()
