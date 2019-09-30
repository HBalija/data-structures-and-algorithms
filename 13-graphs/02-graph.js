class Graph {

  constructor() {
    this.adjacencyList = {};
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
}

const graph = new Graph();

graph.addVertex('Tokyo');
graph.addVertex('Dallas');
graph.addVertex('Aspen');

graph.addEdge('Tokyo', 'Dallas');
graph.addEdge('Dallas', 'Aspen');

console.log(graph.adjacencyList);
// {'Tokyo': ['Dallas'], 'Dallas': ['Tokyo', 'Aspen'], 'Aspen': ['Dallas']}

graph.removeEdge('Tokyo', 'Dallas');

console.log(graph.adjacencyList);
// {'Tokyo': [], 'Dallas': ['Aspen'], 'Aspen': ['Dallas']}


graph.removeVertex('Dallas');
console.log(graph.adjacencyList);
// {'Tokyo': [], 'Aspen': []}
