class WeightedGraph {

  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  addEdge(vertex1, vertex2, weight) {
    if ([vertex1, vertex2].every(item => item in this.adjacencyList)) {
      this.adjacencyList[vertex1].push({ node: vertex2, weight });
      this.adjacencyList[vertex2].push({ node: vertex1, weight });
    }
  }
}

const graph = new WeightedGraph();

graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');

graph.addEdge('A', 'B', 9);
graph.addEdge('A', 'C', 5);
graph.addEdge('B', 'C', 7);

console.log(graph.adjacencyList);
/*
{
  A: [ { node: 'B', weight: 9 }, { node: 'C', weight: 5 } ],
  B: [ { node: 'A', weight: 9 }, { node: 'C', weight: 7 } ],
  C: [ { node: 'A', weight: 5 }, { node: 'B', weight: 7 } ]
}
*/
