class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None
class BinomialHeap:
    def __init__(self):
        self.head = None
    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.degree <= h2.degree:
            head = h1
            h1 = h1.sibling
        else:
            head = h2
            h2 = h2.sibling
        tail = head
        while h1 and h2:
            if h1.degree <= h2.degree:
                tail.sibling = h1
                h1 = h1.sibling
            else:
                tail.sibling = h2
                h2 = h2.sibling
            tail = tail.sibling
        tail.sibling = h1 if h1 else h2
        return head
    def link(self, y, z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1
    def union(self, other):
        new_heap = BinomialHeap()
        new_heap.head = self.merge(self.head, other.head)
        if not new_heap.head:
            return new_heap
        prev = None
        curr = new_heap.head
        next_node = curr.sibling
        while next_node:
            if (curr.degree != next_node.degree or
                (next_node.sibling and next_node.sibling.degree == curr.degree)):
                prev = curr
                curr = next_node
            else:
                if curr.key <= next_node.key:
                    curr.sibling = next_node.sibling
                    self.link(next_node, curr)
                else:
                    if prev:
                        prev.sibling = next_node
                    else:
                        new_heap.head = next_node
                    self.link(curr, next_node)
                    curr = next_node
            next_node = curr.sibling
        return new_heap
    def insert(self, key):
        node = BinomialNode(key)
        temp_heap = BinomialHeap()
        temp_heap.head = node
        self.head = self.union(temp_heap).head
    def find_min(self):
        if not self.head:
            return None
        min_node = self.head
        curr = self.head
        min_key = curr.key
        while curr:
            if curr.key < min_key:
                min_key = curr.key
                min_node = curr
            curr = curr.sibling
        return min_node.key
    def decrease_key(self, node, new_key):
        if new_key > node.key:
            print("New key is greater than current key!")
            return
        node.key = new_key
        y = node
        z = y.parent
        while z and y.key < z.key:
            y.key, z.key = z.key, y.key
            y = z
            z = y.parent
    def find_node(self, node, key):
        if not node:
            return None
        if node.key == key:
            return node
        res = self.find_node(node.child, key)
        if res:
            return res
        return self.find_node(node.sibling, key)
    def delete(self, key):
        node = self.find_node(self.head, key)
        if not node:
            print("Key not found!")
            return
        self.decrease_key(node, float('-inf'))
        self.extract_min()
    def extract_min(self):
        if not self.head:
            return None
        prev_min = None
        min_node = self.head
        prev = None
        curr = self.head
        min_key = curr.key
        while curr:
            if curr.key < min_key:
                min_key = curr.key
                prev_min = prev
                min_node = curr
            prev = curr
            curr = curr.sibling
        if prev_min:
            prev_min.sibling = min_node.sibling
        else:
            self.head = min_node.sibling
        child = min_node.child
        prev = None
        while child:
            next_child = child.sibling
            child.sibling = prev
            child.parent = None
            prev = child
            child = next_child
        new_heap = BinomialHeap()
        new_heap.head = prev
        self.head = self.union(new_heap).head
        return min_key
    def display(self):
        def print_tree(node, level):
            while node:
                print(" " * level * 4 + f"Key: {node.key} (Degree: {node.degree})")
                if node.child:
                    print_tree(node.child, level + 1)
                node = node.sibling

        print("\nCurrent Binomial Heap:")
        if not self.head:
            print("Heap is empty.")
        else:
            print_tree(self.head, 0)


# --- Driver Code ---
if __name__ == "__main__":
    h1 = BinomialHeap()

    print("Enter elements to insert (space-separated):")
    for val in map(int, input().split()):
        h1.insert(val)

    h1.display()

    print("\nMinimum element:", h1.find_min())

    print("\nEnter a key to decrease:")
    k = int(input("Key: "))
    new_k = int(input("New smaller value: "))
    node = h1.find_node(h1.head, k)
    if node:
        h1.decrease_key(node, new_k)
    else:
        print("Key not found!")
    h1.display()

    print("\nEnter key to delete:")
    del_key = int(input())
    h1.delete(del_key)
    h1.display()

    print("\nCreating another heap to perform union:")
    h2 = BinomialHeap()
    for val in [50, 60, 70]:
        h2.insert(val)
    print("Second Heap:")
    h2.display()

    print("\nUnion of both heaps:")
    h1 = h1.union(h2)
    h1.display()
