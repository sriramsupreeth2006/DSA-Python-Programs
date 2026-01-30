class SuffixTreeNode:
    def __init__(self, start, end=None):
        self.children = {}
        self.start = start
        self.end = end
        self.suffix_link = None
        self.index = -1
class SuffixTree:
    def __init__(self, text):
        self.text = text
        self.root = SuffixTreeNode(-1, -1)
        self.size = len(text)
        self.build_suffix_tree()
    def edge_length(self, node):
        return min(node.end, self.position + 1) - node.start
    def build_suffix_tree(self):
        self.position = -1
        self.remaining_suffix_count = 0
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.root.suffix_link = self.root
        self.leaf_end = -1
        self.last_new_node = None
        self.nodes = []
        for i in range(self.size):
            self.extend_suffix_tree(i)
    def extend_suffix_tree(self, pos):
        self.leaf_end = pos
        self.remaining_suffix_count += 1
        self.last_new_node = None
        self.position = pos
        while self.remaining_suffix_count > 0:
            if self.active_length == 0:
                self.active_edge = pos
            if self.text[self.active_edge] not in self.active_node.children:
                leaf = SuffixTreeNode(pos, self.size)
                self.active_node.children[self.text[self.active_edge]] = leaf
                leaf.index = pos - self.remaining_suffix_count + 1
                if self.last_new_node:
                    self.last_new_node.suffix_link = self.active_node
                    self.last_new_node = None
            else:
                next_node = self.active_node.children[self.text[self.active_edge]]
                edge_len = next_node.end - next_node.start
                if self.active_length >= edge_len:
                    self.active_edge += edge_len
                    self.active_length -= edge_len
                    self.active_node = next_node
                    continue
                if self.text[next_node.start + self.active_length] == self.text[pos]:
                    if self.last_new_node and self.active_node != self.root:
                        self.last_new_node.suffix_link = self.active_node
                        self.last_new_node = None
                    self.active_length += 1
                    break
                split = SuffixTreeNode(next_node.start, next_node.start + self.active_length)
                self.active_node.children[self.text[self.active_edge]] = split
                leaf = SuffixTreeNode(pos, self.size)
                split.children[self.text[pos]] = leaf
                leaf.index = pos - self.remaining_suffix_count + 1
                next_node.start += self.active_length
                split.children[self.text[next_node.start]] = next_node
                if self.last_new_node:
                    self.last_new_node.suffix_link = split
                self.last_new_node = split
            self.remaining_suffix_count -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = pos - self.remaining_suffix_count + 1
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link
    def _do_search(self, node, pattern, index):
        if not pattern:
            return True
        if pattern[0] not in node.children:
            return False
        next_node = node.children[pattern[0]]
        edge_str = self.text[next_node.start:min(next_node.end, self.size)]
        edge_len = len(edge_str)
        if len(pattern) <= edge_len:
            return edge_str.startswith(pattern)
        if not pattern.startswith(edge_str):
            return False
        return self._do_search(next_node, pattern[edge_len:], index + edge_len)
    def search(self, pattern):
        return self._do_search(self.root, pattern, 0)
text = input("Enter the string to build suffix tree: ")
stree = SuffixTree(text)
patterns = input("Enter patterns to search separated by space: ").split()
for pat in patterns:
    print(f"Pattern '{pat}' found in text?:", stree.search(pat))
