function Tree(val, left, right) {
  this.left = left;
  this.right = right;
  this.val = val;
}

Tree.prototype[Symbol.iterator] = function* () {
  const queue = [];
  queue.push(this);

  while (queue.length > 0) {
    const node = queue.pop();
    yield node.val;

    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
};

var root = new Tree(1, new Tree(2, new Tree(3)), new Tree(4));
for (var e of root) console.log(e);
