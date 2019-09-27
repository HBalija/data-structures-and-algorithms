class Node {

  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {

  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  push(val) {
    const node = new Node(val);

    if (!this.length) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.length++;
    return this;
  }

  pop() {
    if (!this.length) return undefined;

    const tail = this.tail;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = null;
      tail.prev = null;
    }

    this.length--;
    return tail;
  }

  shift() {
    if (!this.length) return undefined;

    const head = this.head;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = head.next;
      this.head.prev = null;
      head.next = null;
    }

    this.length--;
    return head;
  }

  unshift(val) {
    const node = new Node(val);

    if (!this.length) {
      this.head = node;
      this.tail = node;
    } else {
      this.head.prev = node;
      node.next = this.head;
      this.head = node;
    }

    this.length++;
    return this;
  }

  get(idx) {
    if (idx < 0 || idx >= this.length) return null;

    let element, counter;

    if (idx <= this.length / 2) {
      counter = 0;
      element = this.head;
      while (counter < idx) {
        element = element.next;
        counter++;
      }
    } else {
      counter = this.length - 1;
      element = this.tail;
      while (counter > idx) {
        element = element.prev;
        counter--;
      }
    }
    return element;
  }

  set(idx, val) {
    const node = this.get(idx);

    if (!node) return false;

    node.value = val;
    return true;
  }

  insert(idx, val) {
    if (idx < 0 || idx > this.length) return false;
    if (idx === 0) {
      this.unshift(val);
    } else if (idx === this.length) {
      this.push(val);
    } else {
      const node = new Node(val);
      const nodeBefore = this.get(idx - 1);

      nodeBefore.next.previous = node;
      node.next = nodeBefore.next;

      nodeBefore.next = node;
      node.previous = nodeBefore;

      this.length++;
    }
    return true;
  }

  remove(idx) {
    if (idx < 0 || idx >= this.length) return null;
    if (idx === 0) return this.shift();
    if (idx === this.length - 1) return this.pop();

    const node = this.get(idx);

    node.prev.next = node.next;
    node.next.prev = node.prev;
    node.prev = null;
    node.next = null;

    this.length--;
    return node;
  }

  get str() {
    if (!this.length) return '[ ]';

    let current = this.head;
    let items = '[ ';
    while (current.next) {
      items += `${current.value}, `;
      current = current.next;
    }
    items += `${this.tail.value} ]`;
    return items;
  }
}

const list = new DoublyLinkedList();
list.push(':');
list.push('Hello');
list.push('there');

console.log(list.str);
console.log('head:', list.head.value);
console.log('tail: ', list.tail.value);

console.log(list.remove(1));
console.log(list.str);
console.log('head:', list.head.value);
console.log('tail: ', list.tail.value);
