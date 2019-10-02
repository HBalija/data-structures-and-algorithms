#!/usr/bin/env python3


class WeightedGraph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Add new vertex to adjacency list.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        """
        Add new weighted connection between two vertices.
        """
        if all(key in self.adjacency_list for key in (vertex1, vertex2)):
            self.adjacency_list[vertex1].append(dict(node=vertex2, weight=weight))
            self.adjacency_list[vertex2].append(dict(node=vertex1, weight=weight))


graph = WeightedGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')

graph.add_edge('A', 'B', 9)
graph.add_edge('A', 'C', 5)
graph.add_edge('B', 'C', 7)


print(graph.adjacency_list)
"""
{
    'A': [{'node': 'B', 'weight': 9}, {'node': 'C', 'weight': 5}],
    'B': [{'node': 'A', 'weight': 9}, {'node': 'C', 'weight': 7}],
    'C': [{'node': 'A', 'weight': 5}, {'node': 'B', 'weight': 7}]
}
"""
