class CompressedTrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class CompressedTrie:
    def __init__(self):
        self.root = CompressedTrieNode()
    def insert(self, word):
        current = self.root
        while word:
            for edge in current.children:
                common_prefix_len = self._common_prefix_length(word, edge)
                if common_prefix_len > 0:
                    if common_prefix_len == len(edge):
                        word = word[common_prefix_len:]
                        current = current.children[edge]
                        break
                    else:
                        existing_child = current.children.pop(edge)
                        common_prefix = edge[:common_prefix_len]
                        suffix_existing = edge[common_prefix_len:]
                        suffix_new = word[common_prefix_len:]
                        intermediate = CompressedTrieNode()
                        current.children[common_prefix] = intermediate
                        intermediate.children[suffix_existing] = existing_child
                        if suffix_new:
                            new_node = CompressedTrieNode()
                            new_node.is_end_of_word = True
                            intermediate.children[suffix_new] = new_node
                        else:
                            intermediate.is_end_of_word = True
                        return
            else:
                new_node = CompressedTrieNode()
                new_node.is_end_of_word = True
                current.children[word] = new_node
                return
    def search(self, word):
        current = self.root
        while word:
            found = False
            for edge in current.children:
                if word.startswith(edge):
                    word = word[len(edge):]
                    current = current.children[edge]
                    found = True
                    break
            if not found:
                return False
        return current.is_end_of_word
    def _common_prefix_length(self, s1, s2):
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
            i += 1
        return i
words = input("Enter words separated by space: ").split()
ct = CompressedTrie()
for w in words:
    ct.insert(w)
print("Search 'bear':", ct.search("bear"))
print("Search 'be':", ct.search("be"))
print("Search 'buy':", ct.search("buy"))
print("Search 'stock':", ct.search("stock"))
print("Search 'stop':", ct.search("stop"))
print("Search 'bulls':", ct.search("bulls"))

