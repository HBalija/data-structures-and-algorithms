#!/usr/bin/env python3


class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to adjacency list.
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

    def DFS_recursive(self, starting_node):
        """
        Traverse graph vertices using Depth First Search recursively.
        """
        results = []
        marked = {}

        def helper(vertex):
            if not len(self.adjacency_list[vertex]):
                return

            marked[vertex] = True
            results.append(vertex)
            for item in self.adjacency_list[vertex]:
                if item not in marked:
                    helper(item)

        helper(starting_node)

        return results

    def DFS_iterative(self, starting_node):
        """
        Traverse graph vertices using iterative approach with a help from stack.
        """
        stack = []
        results = []
        marked = {}
        stack.append(starting_node)
        marked[starting_node] = True

        while len(stack):
            vertex = stack.pop()
            results.append(vertex)
            for item in self.adjacency_list[vertex]:
                if item not in marked:
                    marked[item] = True
                    stack.append(item)

        return results

    def BFS_iterative(self, starting_node):
        """
        Traverse graph vertices using Breadth First search.

        Use list as a queue (ignore --> O(n)time for shifting from list).
        """
        queue = []
        results = []
        marked = {}
        queue.append(starting_node)
        marked[starting_node] = True

        while len(queue):
            # pop first item from the queue
            vertex = queue.pop(0)
            results.append(vertex)
            for item in self.adjacency_list[vertex]:
                if item not in marked:
                    marked[item] = True
                    queue.append(item)

        return results


g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_vertex('F')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

"""
graph:

        A
      /   \
     B     C
     |     |
     D --- E
      \   /
        F

"""


print(g.adjacency_list)
"""
{
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}
"""

print(g.DFS_recursive('A'))
# ['A', 'B', 'D', 'E', 'C', 'F']

print(g.DFS_iterative('A'))
"""
results differ from recursive approach because of order
the items are placed in stack - LIFO
['A', 'C', 'E', 'F', 'D', 'B']
"""

print(g.BFS_iterative('A'))
# ['A', 'B', 'C', 'D', 'E', 'F']
