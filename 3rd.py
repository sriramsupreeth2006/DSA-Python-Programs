 # 3. Write a python program to sort the given set of data in descending order using tree sort.(construct BST and do reverse inorder traversal)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right

    def reverse_inorder(self, node, result):
        if node:
            self.reverse_inorder(node.right, result)
            result.append(node.data)
            self.reverse_inorder(node.left, result)

def tree_sort_descending(arr):
    bst = BST()
    for num in arr:
        bst.insert(num)

    sorted_desc = []
    bst.reverse_inorder(bst.root, sorted_desc)
    return sorted_desc

# ----------- Example Usage -----------
data = list(map(int, input("Enter space-separated numbers to sort: ").split()))
sorted_data = tree_sort_descending(data)
print("Sorted in descending order:", sorted_data)
