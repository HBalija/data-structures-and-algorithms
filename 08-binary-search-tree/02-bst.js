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

    while (true) {

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

console.log(tree.contains(10)); // true
console.log(tree.contains(100)); // false
console.log(tree.contains(2)); // true
console.log(tree.contains(17)); // false
