class RBNode:
    def __init__(self, key):
        self.key = key
        self.color = 'red'
        self.left = None
        self.right = None
        self.parent = None
class RedBlackTree:
    def __init__(self):
        self.NULL_LEAF = RBNode(None)
        self.NULL_LEAF.color = 'black'
        self.root = self.NULL_LEAF
    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NULL_LEAF
        new_node.right = self.NULL_LEAF
        parent = None
        current = self.root
        while current != self.NULL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.color = 'red'
        self.fix_insert(new_node)
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL_LEAF:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NULL_LEAF:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    # Case 1
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # Case 2
                        k = k.parent
                        self.left_rotate(k)
                    # Case 3
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    # Mirror Case 1
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # Mirror Case 2
                        k = k.parent
                        self.right_rotate(k)
                    # Mirror Case 3
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
        self.root.color = 'black'
    def search(self, key):
        current = self.root
        while current != self.NULL_LEAF:
            if current.key == key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False
    def inorder_helper(self, node):
        if node != self.NULL_LEAF:
            self.inorder_helper(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder_helper(node.right)
    def inorder(self):
        self.inorder_helper(self.root)
        print()
# Main Program
nums = list(map(int, input("Enter numbers separated by space: ").split()))
rbt = RedBlackTree()

for key in nums:
    rbt.insert(key)

print("Inorder traversal of Red-Black Tree (key and color):")
rbt.inorder()

search_key1 = 30
search_key2 = 11
print(f"Search {search_key1}:", rbt.search(search_key1))
print(f"Search {search_key2}:", rbt.search(search_key2))
