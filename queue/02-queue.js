/*
First in first out.

<--  first -------- last  <--

Singly linked list implementation
*/

class Node {
  constructor(val) {
    this.value = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.size = 0;
    this.first = null;
    this.last = null;
  }


  push(val) {
    const node = new Node(val);

    if (!this.size) {
      this.first = node;
      this.last = node;
    } else {
      this.last.next = node;
      this.last = node;
    }
    this.size++;
    return this.size;
  }

  pop() {
    const node = this.first;
    if (!this.size) return null;
    if (this.first === this.last) {
      this.last = null;
    }
    this.first = this.first.next;
    this.size--;
    return node.value;
  }

  get str() {
    if (!this.size) return '[ ]';

    let current = this.first;
    let items = '[ ';
    while (current.next) {
      items += `${current.value}, `;
      current = current.next;
    }
    items += `${this.last.value} ]`;
    return items;
  }
}


const queue = new Queue();

console.log(queue.size);
console.log('-----------------');
console.log(queue.push('Hey'));
console.log(queue.push('there'));
console.log(queue.push('queue'));
console.log('last: ', queue.last.value);
console.log('first: ', queue.first.value);
console.log(queue.size);
console.log(queue.str);
console.log('-----------------');
console.log(queue.pop());
console.log('last: ', queue.last.value);
console.log('first: ', queue.first.value);
console.log(queue.size);
console.log(queue.str);
console.log('-----------------');
console.log(queue.pop());
console.log('last: ', queue.last.value);
console.log('first: ', queue.first.value);
console.log(queue.size);
console.log(queue.str);
console.log('-----------------');
console.log(queue.pop());
console.log(queue.size);
console.log(queue.str);
