#!/usr/bin/env python3

"""
Dijkstra shortest path algorithm using binary heap as priority queue.

Insertion and removal - O(log n)time.
"""


class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.values = []

    def __str__(self):
        return str([(item.val, item.priority) for item in self.values])

    def enqueue(self, value, priority):
        """
        Add new node to priority queue.
        """
        new_node = Node(value, priority)
        self.values.append(new_node)
        self.bubble_up()

    def bubble_up(self):
        """
        Place value to its position based on priority.
        """
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = self.values[parent_idx]
            if element.priority >= parent.priority:
                break
            self.values[parent_idx] = element
            self.values[idx] = parent
            idx = parent_idx

    def dequeue(self):
        """
        Remove first element from queue.
        """
        start = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return start

    def sink_down(self):
        """
        Set last element to be the first and bubble
        down to position based on priority.
        """
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            left_child = None
            right_child = None
            swap = None

            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child.priority < element.priority:
                    swap = left_child_idx
            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((not swap and right_child.priority < element.priority) or
                        (swap and right_child.priority < left_child.priority)):
                    swap = right_child_idx
            if (not swap):
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap


class WeightedGraph:

    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Add a new vertex to adjacency list.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        """
        Add a new weighted connection between two vertices.
        """
        if all(key in self.adjacency_list for key in (vertex1, vertex2)):
            self.adjacency_list[vertex1].append(dict(node=vertex2, weight=weight))
            self.adjacency_list[vertex2].append(dict(node=vertex1, weight=weight))

    def dijkstra(self, start, finish):
        """
        Find the shortest path between two nodes using Dijkstra.
        """
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []
        smallest = None
        visited = []

        if not all(item in self.adjacency_list for item in [start, finish]):
            return None

        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
            previous[vertex] = None

        while len(nodes.values):
            smallest = nodes.dequeue().value

            if smallest in visited:
                continue

            visited.append(smallest)

            if smallest == finish:
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]

            if distances[smallest] != float('inf'):
                for next_node in self.adjacency_list[smallest]:
                    candidat_distance = distances[smallest] + next_node['weight']
                    next_neighbor = next_node['node']
                    if candidat_distance < distances[next_neighbor]:
                        distances[next_neighbor] = candidat_distance
                        previous[next_neighbor] = smallest
                        nodes.enqueue(next_neighbor, candidat_distance)

        return ([start] + path[::-1], distances[finish])


graph = WeightedGraph()

graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')


graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'E', 3)
graph.add_edge('C', 'D', 2)
graph.add_edge('D', 'E', 3)
graph.add_edge('D', 'F', 1)
graph.add_edge('E', 'F', 1)

"""
{
    A: [{node: 'B', weight: 4}, {node: 'C', weight: 2}],
    B: [{node: 'A', weight: 4}, {node: 'E', weight: 3}],
    C: [{node: 'A', weight: 2}, {node: 'D', weight: 2}],
    D: [{node: 'C', weight: 2}, {node: 'E', weight: 3}, {node: 'F', weight: 1}],
    E: [{node: 'B', weight: 3}, {node: 'D', weight: 3}, {node: 'F', weight: 1}],
    F: [{node: 'D', weight: 1}, {node: 'E', weight: 1}]}
"""

print(graph.dijkstra('A', 'E'))
# (['A', 'C', 'D', 'F', 'E'], 6)
