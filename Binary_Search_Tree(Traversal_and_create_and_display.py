class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                parent = temp
                if data < temp.data:
                    temp = temp.lchild
                else:
                    temp = temp.rchild
            if data < parent.data:
                parent.lchild = new_node
            else:
                parent.rchild = new_node
    def inorder(self, t):
        if t:
            self.inorder(t.lchild)
            print(t.data, end=" ")
            self.inorder(t.rchild)
    def preorder(self, t):
        if t:
            print(t.data, end=" ")
            self.preorder(t.lchild)
            self.preorder(t.rchild)
    def postorder(self, t):
        if t:
            self.postorder(t.lchild)
            self.postorder(t.rchild)
            print(t.data, end=" ")
    def traversal(self):
        while True:
            print("\n1. Preorder\n2. Inorder\n3. Postorder\n4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("Preorder sequence:")
                self.preorder(self.root)
            elif choice == 2:
                print("Inorder sequence:")
                self.inorder(self.root)
            elif choice == 3:
                print("Postorder sequence:")
                self.postorder(self.root)
            elif choice == 4:
                break
            else:
                print("Invalid choice!")
bst = BST()
while True:
    data = int(input("Enter data (or -1 to stop): "))
    if data == -1:
        break
    bst.insert(data)

bst.traversal()
