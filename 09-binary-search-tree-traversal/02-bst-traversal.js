class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  insert(value) {
    const node = new Node(value);

    if (!this.root) {
      this.root = node;
      return this;
    }

    let current = this.root;

    while (true) { // eslint-disable-line no-constant-condition

      if (value === current.value) return null;

      if (value < current.value) {
        if (!current.left) {
          current.left = node;
          return this;
        }
        // move to the next left
        current = current.left;
      } else if (value > current.value) {
        if (!current.right) {
          current.right = node;
          return this;
        }
        // move to the next right
        current = current.right;
      }
    }
  }

  contains(value) {
    if (!this.root) return false;

    let current = this.root;

    while (current) { // eslint-disable-line no-constant-condition
      if (value === current.value) return true;

      if (value < current.value) {
        current = current.left; // move to the next left
      } else if (value > current.value) {
        current = current.right;  // move to the next right
      }
    }
    return false;
  }

  get BFS() {
    const queue = [];
    const values = [];
    let dequeued;

    queue.push(this.root);

    while (queue.length) {
      dequeued = queue.shift();
      values.push(dequeued.value);
      dequeued.left && queue.push(dequeued.left);
      dequeued.right && queue.push(dequeued.right);
    }
    return values;
  }

  get DFSpreOrder() {
    const values = [];

    const traverse = node => {
      values.push(node.value);
      node.left && traverse(node.left);
      node.right && traverse(node.right);
    };

    traverse(this.root);

    return values;
  }

  get DFSpostOrder() {
    const values = [];

    const traverse = node => {
      node.left && traverse(node.left);
      node.right && traverse(node.right);
      values.push(node.value);
    };

    traverse(this.root);

    return values;
  }

  get DFSinOrder() {
    const values = [];

    const traverse = node => {
      node.left && traverse(node.left);
      values.push(node.value);
      node.right && traverse(node.right);
    };

    traverse(this.root);

    return values;
  }
}


const tree = new BinarySearchTree();

tree.insert(10);
tree.insert(5);
tree.insert(13);
tree.insert(11);
tree.insert(2);
tree.insert(16);
tree.insert(7);
tree.insert(7);

/*
tree representation

                  10
          5                 13
      2       7         11      16

*/

console.log(tree.BFS);  // [ 10, 5, 13, 2, 7, 11, 16 ]
console.log(tree.DFSpreOrder);  // [ 10, 5, 2, 7, 13, 11, 16 ]
console.log(tree.DFSpostOrder);  // [ 2, 7, 5, 11, 16, 13, 10 ]
console.log(tree.DFSinOrder);  // [ 2, 5, 7, 10, 11, 13, 16 ]
