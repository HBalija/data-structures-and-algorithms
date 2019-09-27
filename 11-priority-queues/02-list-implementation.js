/*
Priority queue - Array

Sort O(n log n)time
Dequeue O(n)time
*/

class PriorityQueue {

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


const q = new PriorityQueue();

q.enqueue('B', 3);
q.enqueue('C', 5);
q.enqueue('D', 2);
q.enqueue('Q', 20);
q.enqueue('P', 1.5);

console.log(q.values);

/*
values sorted based on priority

[ { val: 'P', priority: 1.5 },
  { val: 'D', priority: 2 },
  { val: 'B', priority: 3 },
  { val: 'C', priority: 5 },
  { val: 'Q', priority: 20 } ]
*/
