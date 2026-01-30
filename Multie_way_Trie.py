class TrieNode:
    def __init__(self):
        self.children = {} 
        self.is_end_of_word = False
class MultiWayTrie:
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
    def _delete_helper(self, node, word, depth):
        if not node:
            return False
        if depth == len(word):
            if node.is_end_of_word:
                node.is_end_of_word = False
            return len(node.children) == 0
        ch = word[depth]
        if ch in node.children:
            should_delete_child = self._delete_helper(node.children[ch], word, depth + 1)
            if should_delete_child:
                del node.children[ch]
                return (not node.is_end_of_word) and (len(node.children) == 0)
        return False
    def delete(self, word):
        self._delete_helper(self.root, word, 0)
words = input("Enter words separated by space: ").split()
trie = MultiWayTrie()
for word in words:
    trie.insert(word)
print("Search 'apple':", trie.search('apple'))
print("Search 'app':", trie.search('app'))
word_to_delete = input("Enter word to delete: ")
trie.delete(word_to_delete)
print(f"After deletion, search '{word_to_delete}':", trie.search(word_to_delete))
