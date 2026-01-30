class SegmentTreeLazy:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(data, 0, self.n - 1, 0)
    def _build(self, data, start, end, node):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, start, mid, 2 * node + 1)
            self._build(data, mid + 1, end, 2 * node + 2)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    def _update_range(self, start, end, l, r, val, node):
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if start > r or end < l:
            return
        if start >= l and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                self.lazy[2 * node + 1] += val
                self.lazy[2 * node + 2] += val
            return
        mid = (start + end) // 2
        self._update_range(start, mid, l, r, val, 2 * node + 1)
        self._update_range(mid + 1, end, l, r, val, 2 * node + 2)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    def update_range(self, l, r, val):
        self._update_range(0, self.n - 1, l, r, val, 0)
    def _query_range(self, start, end, l, r, node):
        if start > r or end < l:
            return 0
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if start >= l and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self._query_range(start, mid, l, r, 2 * node + 1)
        right_sum = self._query_range(mid + 1, end, l, r, 2 * node + 2)
        return left_sum + right_sum
    def query_range(self, l, r):
        return self._query_range(0, self.n - 1, l, r, 0)
arr = list(map(int, input("Enter array elements separated by space: ").split()))
seg_tree = SegmentTreeLazy(arr)
print("Sum of values in range(1, 3):", seg_tree.query_range(1, 3))  
seg_tree.update_range(1, 5, 11)  
print("Sum of values in range(1, 3) after update:", seg_tree.query_range(1, 3))
print("Sum of values in range(0, 5):", seg_tree.query_range(0, 5))
