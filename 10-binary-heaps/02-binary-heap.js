class MaxBinaryHeap {

  constructor() {
    this.values = [];
  }

  insert(value) {
    this.values.push(value);

    if (this.values.length === 1) return;

    let idx = this.values.length - 1;

    // bubble up
    while (idx > 0) {
      const parentIdx = Math.floor((idx - 1) / 2);
      if (this.values[parentIdx] > this.values[idx]) break;
      // swap values
      const temp = this.values[parentIdx];
      this.values[parentIdx] = this.values[idx];
      this.values[idx] = temp;

      // set idx to be parentIdx
      idx = parentIdx;
    }
  }

  extractMax() {
    // pop last element and place it as a first one; this value will be swapped in bubble down
    const max = this.values[0];
    const bubbleDownValue = this.values.pop();
    this.values[0] = bubbleDownValue;

    // bubble down
    let idx = 0;
    while (true) {  // eslint-disable-line no-constant-condition
      const leftChildIdx = 2 * idx + 1;
      const rightChildIdx = 2 * idx + 2;

      const leftChild = leftChildIdx < this.values.length && this.values[leftChildIdx];
      const rightChild = rightChildIdx < this.values.length && this.values[rightChildIdx];
      // index of child node with greater value
      const swapIdx = leftChild > rightChild ? leftChildIdx : rightChildIdx;

      // stop swapping if bubble value greater than swapIdx value --> list sorted
      if (this.values[swapIdx] <= bubbleDownValue) break;

      this.values[idx] = this.values[swapIdx];
      this.values[swapIdx] = bubbleDownValue;
      idx = swapIdx;
    }
    return max;
  }

}


const heap = new MaxBinaryHeap();

heap.insert(33);
heap.insert(41);
heap.insert(27);
heap.insert(39);
heap.insert(12);
heap.insert(18);
heap.insert(55);


console.log(heap.values); // [ 55, 39, 41, 33, 12, 18, 27 ]

/*
              55
      39              41
  33      12      18        27
*/

heap.extractMax();

console.log(heap.values); // [ 41, 39, 27, 33, 12, 18 ]
