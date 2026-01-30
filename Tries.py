class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.is_end_of_word = True
    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.is_end_of_word
    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True
words = input("Enter words separated by spaces: ").split()
trie = Trie()
for w in words:
    trie.insert(w)
print("Search 'app':", trie.search("app"))
print("Search 'bat':", trie.search("bat"))
print("Search 'batman':", trie.search("batman"))
print("Starts with 'ba':", trie.starts_with("ba"))
