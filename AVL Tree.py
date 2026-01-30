class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        balance = self.get_balance(root)
        # Left Left
        if balance > 1 and key < root.left.key:
            print(f"LL Rotation on insert({key})")
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and key > root.right.key:
            print(f"RR Rotation on insert({key})")
            return self.left_rotate(root)
        # Left Right
        if balance > 1 and key > root.left.key:
            print(f"LR Rotation on insert({key})")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Left
        if balance < -1 and key < root.right.key:
            print(f"RL Rotation on insert({key})")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        if not root:
            return root
        # Update height
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        # Balance
        balance = self.get_balance(root)
        # Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            print(f"LL Rotation on delete({key})")
            return self.right_rotate(root)
        # Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            print(f"LR Rotation on delete({key})")
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            print(f"RR Rotation on delete({key})")
            return self.left_rotate(root)
        # Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            print(f"RL Rotation on delete({key})")
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
    def get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y
    def get_height(self, node):
        return node.height if node else 0
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"{root.key} ", end='')
            self.inorder_traversal(root.right)
tree = AVLTree()
root = None

while True:
    print("\n=== AVL Tree Menu ===")
    print("1. Insert element")
    print("2. Delete element")
    print("3. Display inorder traversal")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            key = int(input("Enter value to insert: "))
            root = tree.insert(root, key)
        except ValueError:
            print("Invalid input. Please enter an i nteger.")
    elif choice == '2':
        try:
            key = int(input("Enter value to delete: "))
            root = tree.delete(root, key)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    elif choice == '3':
        print("Inorder traversal of AVL Tree:")
        tree.inorder_traversal(root)
        print()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
