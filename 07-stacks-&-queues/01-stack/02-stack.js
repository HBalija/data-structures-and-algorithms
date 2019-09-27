/*
Last in first out.

-->
<--   last ---------------------- first

Singly linked list implementation
*/

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(val) {
    const node = new Node(val);

    if (!this.size) {
      this.first = node;
      this.last = node;
    } else {
      node.next = this.last;
      this.last = node;
    }

    this.size++;
    return this.size;
  }

  pop() {
    if (!this.size) return null;

    const node = this.last;
    if (this.last === this.first) {
      this.first = null;
    }
    this.last = node.next; // null if only 1
    node.next = null; // clean the reference of popped element
    this.size--;
    return node.value;
  }

  get str() {
    if (!this.size) return '[ ]';

    let current = this.last;
    let items = '[ ';
    while (current.next) {
      items += `${current.value}, `;
      current = current.next;
    }
    items += `${this.first.value} ]`;
    return items;
  }
}


const stack = new Stack();

console.log(stack.size);
console.log('-----------------');
console.log(stack.push('Hey'));
console.log(stack.push('there'));
console.log(stack.push('stack'));
console.log('last: ', stack.last.value);
console.log('first: ', stack.first.value);
console.log(stack.size);
console.log(stack.str);
console.log(stack.pop());
console.log('last: ', stack.last.value);
console.log('first: ', stack.first.value);
console.log(stack.size);
console.log(stack.str);
console.log(stack.pop());
console.log('last: ', stack.last.value);
console.log('first: ', stack.first.value);
console.log(stack.size);
console.log(stack.str);
console.log(stack.pop());
console.log(stack.size);
console.log(stack.str);
