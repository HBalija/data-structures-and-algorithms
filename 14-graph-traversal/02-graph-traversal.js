class Graph {

  constructor() {
    this.adjacencyList = {};
    this.marked = {};
    this.results = [];
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  addEdge(vertex1, vertex2) {
    if ([vertex1, vertex2].every(item => item in this.adjacencyList)) {
      this.adjacencyList[vertex2].push(vertex1);
      this.adjacencyList[vertex1].push(vertex2);
    }
  }

  removeEdge(vertex1, vertex2) {
    if ([vertex1, vertex2].every(item => item in this.adjacencyList)) {
      this.adjacencyList[vertex1] = this.adjacencyList[vertex1].filter(item => item !== vertex2);
      this.adjacencyList[vertex2] = this.adjacencyList[vertex2].filter(item => item !== vertex1);
    }
  }

  removeVertex(vertex) {
    if (vertex in this.adjacencyList) {
      for (const item of this.adjacencyList[vertex]) {
        this.removeEdge(item, vertex);
      }
      delete this.adjacencyList[vertex];
    }
  }

  DFSRecursive(startingNode) {
    const results = [];
    const marked = [];

    const helper = vertex => {

      if (!this.adjacencyList[vertex].length) return;

      marked[vertex] = true;
      results.push(vertex);
      for (const item of this.adjacencyList[vertex]) {
        if (!(item in marked)) {
          helper(item);
        }
      }
    };

    helper(startingNode);

    return results;
  }

  DFSIterative(startingNode) {
    const stack = [];
    const results = [];
    const marked = {};
    stack.push(startingNode);
    marked[startingNode] = true;

    while (stack.length) {
      const vertex = stack.pop();
      results.push(vertex);
      this.adjacencyList[vertex].forEach(element => {
        if (!(element in marked)) {
          marked[element] = true;
          stack.push(element);
        }
      });
    }
    return results;
  }

  BFSIterative(startingNode) {
    const queue = [];
    const results = [];
    const marked = {};
    queue.push(startingNode);
    marked[startingNode] = true;

    while (queue.length) {
      const vertex = queue.shift();
      results.push(vertex);
      for (const item of this.adjacencyList[vertex]) {
        if (!(item in marked)) {
          marked[item] = true;
          queue.push(item);
        }
      }
    }
    return results;
  }

}


const g = new Graph();

g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');

g.addEdge('A', 'B');
g.addEdge('A', 'C');
g.addEdge('B', 'D');
g.addEdge('C', 'E');
g.addEdge('D', 'E');
g.addEdge('D', 'F');
g.addEdge('E', 'F');

/*
graph:

        A
      /   \
     B     C
     |     |
     D --- E
      \   /
        F

*/

console.log(g.adjacencyList);
/*
{
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}
*/

console.log(g.DFSRecursive('A'));
/*
['A', 'B', 'D', 'E', 'C', 'F']
*/


console.log(g.DFSIterative('A'));
/*
results differ from recursive approach because of order
the items are placed in stack - LIFO
['A', 'C', 'E', 'F', 'D', 'B']
*/

console.log(g.BFSIterative('A'));
// ['A', 'B', 'C', 'D', 'E', 'F']
