class Node {

  constructor(val) {
    this.val = val;
    this.next = null;
  }
}


class SinglyLinkedList {

  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  push(val) {
    const node = new Node(val);

    if (!this.head) this.head = node;
    else this.tail.next = node;

    this.tail = node;
    this.length++;

    return this;
  }

  pop() {
    if (!this.length) return undefined;

    let newTail = this.head;
    const tail = this.tail;


    while (newTail.next && newTail.next !== tail) {
      newTail = newTail.next;
    }

    newTail.next = null;
    this.tail = newTail;
    this.length--;

    if (!this.length) {
      this.head = null;
      this.tail = null;
    }

    return tail;
  }

  shift() {
    if (!this.length) return undefined;

    const oldHead = this.head;
    this.head = oldHead.next;
    this.length--;

    if (!this.length) this.tail = null;

    return oldHead;
  }

  unshift(val) {
    const node = new Node(val);

    if (!this.length) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }

    this.length++;

    return this;
  }

  get(idx) {

    if (idx < 0 || idx >= this.length) return null;

    let element = this.head;
    let counter = 0;

    while (counter < idx) {
      element = element.next;
      counter++;
    }
    return element;
  }

  set(idx, value) {

    const node = this.get(idx);

    if (!node) return false;

    console.log(node);
    node.val = value;
    return true;
  }

  insert(idx, value) {

    if (idx < 0 || idx > this.length) return false;

    if (idx === this.length) {
      this.push(value);
    } else if (idx === 0) {
      this.unshift(value);
    } else {
      const nodeBefore = this.get(idx - 1);
      const nodeAfter = nodeBefore.next;

      const newNode = new Node(value);
      nodeBefore.next = newNode;
      newNode.next = nodeAfter;
      this.length++;
    }

    return true;
  }

  remove(idx) {
    if (idx < 0 || idx >= this.length) return undefined;

    if (idx === this.length - 1) return this.pop();
    if (idx === 0) return this.shift();

    const nodeBefore = this.get(idx - 1);
    const node = nodeBefore.next;
    nodeBefore.next = node.next;
    this.length--;
    return node;
  }

  reverse() {

    let node = this.head;
    this.head = this.tail;
    this.tail = node;

    let next, prev;

    for (let i = 0; i < this.length; i++) {
      next = node.next;
      node.next = prev;
      prev = node;
      node = next;
    }
    return this;
  }

  get str() {
    if (!this.length) return '[ ]';

    let current = this.head;
    let items = '[ ';
    while (current.next) {
      items += `${current.val}, `;
      current = current.next;
    }
    items += `${this.tail.val} ]`;
    return items;
  }
}
