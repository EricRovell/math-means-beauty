class Tree {
  constructor() {
    this.root = null;
  }

  add(value) {
    let node = new Node(value);
    (this.root == null) ? this.root = node : this.root.addNode(node);
  }

  get traverse() {
    let values = new Array;
    this.root.visit(values);
    return values;
  }

  search(value) {
    return this.root.search(value);
  }
}

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  addNode(node) {
    if (node.value < this.value) {
      (this.left == null) ? this.left = node : this.left.addNode(node);
    } else if (node.value > this.value) {
      (this.right == null) ? this.right = node : this.right.addNode(node);
    }
  }

  visit(values) {
      if (this.left != null) { this.left.visit(values); }
      values.push(this.value);
      if (this.right != null) { this.right.visit(values); }
  }

  search(value) {
    if (value == this.value) {
      return true;
    } else if (value < this.value && this.left != null) {
      return this.left.search(value);
    } else if (value > this.value && this.right != null) {
      return this.right.search(value);
    } else {
      return false;
    }
  }
}


let tree = new Tree();
tree.add(5);
tree.add(6);
tree.add(4);
tree.add(18);
tree.add(1);
tree.search(4);