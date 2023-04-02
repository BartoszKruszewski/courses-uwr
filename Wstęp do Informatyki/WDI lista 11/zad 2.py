class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def tree_len(t):
    if t is None:
        return 0
    else:
        return 1 + tree_len(t.left) + tree_len(t.right)

def tree_height(t):
    if t is None:
        return 0
    return 1 + max(tree_height(t.left), tree_height(t.right))

def add(t, value):
    first = t
    is_running = True
    while is_running:
        if value >= t.val:
            if t.right is None:
                t.right = TreeItem(value)
                is_running = False
            else:
                t = t.right
        else:
            if t.left is None:
                t.left = TreeItem(value)
                is_running = False
            else:
                t = t.left
    return first


def print_tree(t, depth=0):
    if t is not None:
        print(str(t.val), end=" ")
        print_tree(t.left, depth + 1)
        print_tree(t.right, depth + 1)

def print_tree_BST(t):
    if t is not None:
        print_tree_BST(t.left)
        if t.val > 0:
            print(t.val, end=" ")
        print_tree_BST(t.right)

def is_BST_tree(t):
    if t is None:
        return True
    if (t.left is None or t.left.val <= t.val) and (t.right is None or t.right.val >= t.val):
        return is_BST_tree(t.left) and is_BST_tree(t.right)
    return False

def merge_BST(t1, t2):
    root = t2
    while t2.left is not None:
        t2 = t2.left
    t2.left = t1
    return root


tree1 = TreeItem(3)
tree2 = TreeItem(-10)
for i in range(-5,7):
    tree1 = add(tree1, i)
for i in range(-15,-10):
    tree2 = add(tree2, i)
print_tree(tree1)
print()
print_tree(tree2)
print()
print(print_tree(merge_BST(tree2, tree1)))
