class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None
    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)
    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BPlusTreeNode(t, y.leaf)
        z.keys = y.keys[t:]  
        y.keys = y.keys[:t]  
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        else:
            z.next = y.next
            y.next = z
        self.children.insert(i + 1, z)
        self.keys.insert(i, z.keys[0])  
    def search(self, key):
        i = 0
        while i < len(self.keys) and key >= self.keys[i]:
            i += 1
        if self.leaf:
            return key in self.keys
        else:
            return self.children[i].search(key)
    def traverse_leaves(self):
        node = self
        while not node.leaf:
            node = node.children[0]
        while node:
            for key in node.keys:
                print(key, end=' ')
            node = node.next
        print()
class BPlusTree:
    def __init__(self, t):
        self.t = t
        self.root = BPlusTreeNode(t, leaf=True)
    def insert(self, key):
        r = self.root
        if len(r.keys) == 2 * self.t - 1:
            s = BPlusTreeNode(self.t, leaf=False)
            s.children.append(r)
            s.split_child(0)
            i = 0
            if s.keys[0] < key:
                i += 1
            s.children[i].insert_non_full(key)
            self.root = s
        else:
            r.insert_non_full(key)
    def search(self, key):
        return self.root.search(key)
    def traverse_leaves(self):
        self.root.traverse_leaves()
nums = list(map(int, input("Enter numbers separated by space: ").split()))
bptree = BPlusTree(2)
for key in nums:
    bptree.insert(key)
print("B+ Tree leaf node traversal:")
bptree.traverse_leaves()
print("Search 100 in B+ Tree:", bptree.search(100))
print("Search 59 in B+ Tree:", bptree.search(59))
