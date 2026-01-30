class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  
        self.leaf = leaf
        self.keys = []  
        self.children = []  
    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.leaf:
            self.keys.append(None)
            while i >= 0 and key < self.keys[i]:
                self.keys[i+1] = self.keys[i]
                i -= 1
            self.keys[i+1] = key
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
        z = BTreeNode(t, y.leaf)
        z.keys = y.keys[t:]  
        y.keys = y.keys[:t - 1]  
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())
    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and self.keys[i] == key:
            return True
        if self.leaf:
            return False
        return self.children[i].search(key)
    def traverse(self):
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], end=' ')
        if not self.leaf:
            self.children[len(self.keys)].traverse()
class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, leaf=True)
    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            s = BTreeNode(self.t, leaf=False)
            s.children.insert(0, root)
            s.split_child(0)
            i = 0
            if s.keys[0] < key:
                i += 1
            s.children[i].insert_non_full(key)
            self.root = s
        else:
            root.insert_non_full(key)
    def search(self, key):
        return self.root.search(key)

    def traverse(self):
        self.root.traverse()
        print()
num = list(map(int, input("Enter numbers sperated by spaces:").split()))
btree = BTree(2)
for key in num:
    btree.insert(key)
print("B-Tree traversal:")
btree.traverse()
print("Search 69 in B-Tree:", btree.search(69))
print("Search 124 in B-Tree:", btree.search(124))
