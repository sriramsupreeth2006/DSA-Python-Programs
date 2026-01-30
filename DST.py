class DSTNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
class DigitalSearchTree:
    def __init__(self):
        self.root = None
    def _get_bit(self, key, bit_index):
        byte_index = bit_index // 8
        bit_position = 7 - (bit_index % 8)
        if byte_index >= len(key):
            return 0
        return (ord(key[byte_index]) >> bit_position) & 1
    def insert(self, key):
        if self.root is None:
            self.root = DSTNode(key)
            return
        current = self.root
        i = 0
        while True:
            if current.key == key:
                return
            bit_current = self._get_bit(current.key, i)
            bit_key = self._get_bit(key, i)
            if bit_key == bit_current:
                if bit_key == 0:
                    if current.left is None:
                        current.left = DSTNode(key)
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = DSTNode(key)
                        return
                    current = current.right
                i += 1
            else:
                break
    def search(self, key):
        current = self.root
        i = 0
        while current:
            if current.key == key:
                return True
            bit_current = self._get_bit(current.key, i)
            bit_key = self._get_bit(key, i)
            if bit_key == bit_current:
                if bit_key == 0:
                    current = current.left
                else:
                    current = current.right
                i += 1
            else:
                return False
        return False
words = input("Enter words separated by spaces: ").split()
dst = DigitalSearchTree()
for w in words:
    dst.insert(w)
print("Search 'bean':", dst.search("bean"))
print("Search 'stopper':", dst.search("stopper"))
