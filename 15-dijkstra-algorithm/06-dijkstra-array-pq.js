/*
Dijkstra shortest path algorithm using array as priority queue.
*/

class PriorityQueue {
  // Not very efficient - sort() --> O(n)time

  constructor() {
    this.values = [];
  }

  enqueue(val, priority) {
    this.values.push({ val, priority });
    this.sort();
  }

  dequeue() {
    return this.values.shift();
  }

  sort() {
    this.values.sort((a, b) => a.priority - b.priority);
  }
}


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

  dijkstra(start, finish) {
    const nodes = new PriorityQueue();
    const distances = {}; // distances from starting node to visiting nodes
    const previous = {}; // fastest way from starting node to visiting node --> through node
    const visited = [];  // array that tracks visited nodes
    const path = []; // array to return at end
    let smallest;

    // check that both start and finish are in adjacencyList
    if (![start, finish].every(item => item in this.adjacencyList)) return null;

    /* build up initial state:
      - set distances to infinity, 0 for starting node
      - add values to priority queue --> priority 0 for start
      - set previous for all vertices to be null
    */
    for (const vertex in this.adjacencyList) {
      if (vertex === start) {
        distances[vertex] = 0;
        nodes.enqueue(vertex, 0);
      } else {
        distances[vertex] = Infinity;
      }
      previous.vertex = null;
    }

    /* while nodes in priority queue:
      - dequeue a vertex (return a value of vertex with smallest priority)
      - check if that node is already visited; if yes skip iteration, if not mark it as visited
      - if that vertex is the same as ending vertex --> we are done
        - build up path array to return in the end
      - find neighboring node:
        - calculate new distance to neighbouring node (using previous)
          -  if smaller than previous distance for that neighbouring node
            - store it (line 82)
            - update previous for that node with current iterating node (line 83)
            - enqueue neighbor node in priority queue with new priority of candidatDistance
    */
    while (nodes.values.length) {
      smallest = nodes.dequeue().val; // 'A', 'B' ....

      if (visited.includes(smallest)) continue;
      visited.push(smallest);

      if (smallest === finish) {
        while (previous[smallest]) {
          path.push(smallest);
          smallest = previous[smallest];
        }
      }

      if (smallest || distances[smallest] !== Infinity) {
        for (const nextNode of this.adjacencyList[smallest]) {
          const candidateDistance = distances[smallest] + nextNode.weight;
          const nextNeighbor = nextNode.node; // 'A', 'B' ....
          if (candidateDistance < distances[nextNeighbor]) {
            distances[nextNeighbor] = candidateDistance;
            previous[nextNeighbor] = smallest;
            nodes.enqueue(nextNeighbor, candidateDistance);
          }
        }
      }
    }
    // return reversed path array and add starting node as first element and total shortest distance
    return [path.concat(start).reverse(), distances[finish]];
  }
}


const graph = new WeightedGraph();

graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addVertex('E');
graph.addVertex('F');


graph.addEdge('A', 'B', 4);
graph.addEdge('A', 'C', 2);
graph.addEdge('B', 'E', 3);
graph.addEdge('C', 'D', 2);
graph.addEdge('D', 'E', 3);
graph.addEdge('D', 'F', 1);
graph.addEdge('E', 'F', 1);

/*
{
  A: [ { node: 'B', weight: 4 }, { node: 'C', weight: 2 } ],
  B: [ { node: 'A', weight: 4 }, { node: 'E', weight: 3 } ],
  C: [ { node: 'A', weight: 2 }, { node: 'D', weight: 2 } ],
  D: [ { node: 'C', weight: 2 }, { node: 'E', weight: 3 }, { node: 'F', weight: 1 } ],
  E: [ { node: 'B', weight: 3 }, { node: 'D', weight: 3 }, { node: 'F', weight: 1 } ],
  F: [ { node: 'D', weight: 1 }, { node: 'E', weight: 1 } ] }

*/

console.log(graph.dijkstra('A', 'E'));
// [['A', 'C', 'D', 'E', 'F], 6]
