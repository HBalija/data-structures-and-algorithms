#!/usr/bin/env python3


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to adjacency list.

        Vertex consists of a key (vertex name) with list value of its edges.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """
        Add a new connection between two vertices.

        This is undirected graph. To make it directed, add only one connection.
        """
        if all(key in self.adjacency_list for key in (vertex1, vertex2)):
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        """
        Remove connection between two vertices.

        Undirected graph - connections in both direction needs to be removed.
        """
        if all(key in self.adjacency_list for key in (vertex1, vertex2)):
            self.adjacency_list[vertex1] = [
                item for item in self.adjacency_list[vertex1] if item != vertex2]
            self.adjacency_list[vertex2] = [
                item for item in self.adjacency_list[vertex2] if item != vertex1]

    def remove_vertex(self, vertex):
        """
        Remove a vertex from graph.

        First remove all connections to other vertices and then delete
        the vertex itself.
        """
        if vertex in self.adjacency_list:
            for element in self.adjacency_list[vertex]:
                self.remove_edge(element, vertex)
            del self.adjacency_list[vertex]


graph = Graph()

graph.add_vertex('Tokyo')
graph.add_vertex('Dallas')
graph.add_vertex('Aspen')

graph.add_edge('Tokyo', 'Dallas')
graph.add_edge('Dallas', 'Aspen')

print(graph.adjacency_list)
# {'Tokyo': ['Dallas'], 'Dallas': ['Tokyo', 'Aspen'], 'Aspen': ['Dallas']}

graph.remove_edge('Tokyo', 'Dallas')

print(graph.adjacency_list)
# {'Tokyo': [], 'Dallas': ['Aspen'], 'Aspen': ['Dallas']}

graph.remove_vertex('Dallas')
print(graph.adjacency_list)
# {'Tokyo': [], 'Aspen': []}
