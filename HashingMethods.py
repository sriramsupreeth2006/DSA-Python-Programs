class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
class HashFunctions:
    def __init__(self, table_size):
        self.table_size = table_size
        self.table = [None] * table_size
    def division_method(self, key):
        return key % self.table_size
    def multiplication_method(self, key):
        A = 0.6180339887
        return int(self.table_size * ((key * A) % 1))
    def mid_square_method(self, key):
        square = key * key
        mid = str(square)
        if len(mid) < 2:
            mid_val = int(mid)
        else:
            start = len(mid) // 2 - 1
            mid_val = int(mid[start:start+2])
        return mid_val % self.table_size
    def folding_method(self, key):
        key_str = str(key)
        parts = [key_str[i:i+2] for i in range(0, len(key_str), 2)]
        total = sum(int(part) for part in parts)
        return total % self.table_size
    def insert(self, key, method="division"):
        if method == "division":
            index = self.division_method(key)
        elif method == "multiplication":
            index = self.multiplication_method(key)
        elif method == "mid_square":
            index = self.mid_square_method(key)
        elif method == "folding":
            index = self.folding_method(key)
        else:
            raise ValueError("Invalid hashing method!")
        new_node = Node(key)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = new_node
    def display(self):
        for i in range(self.table_size):
            print(f"Index {i}:", end=" ")
            current = self.table[i]
            if current is None:
                print("None")
            else:
                while current:
                    print(f"{current.key} -> ", end="")
                    current = current.next
                print("None")
if __name__ == "__main__":
    table_size = int(input("Enter hash table size: "))
    hash_table = HashFunctions(table_size)
    keys = list(map(int, input("Enter keys separated by spaces: ").split()))
    print("\nChoose hashing method:")
    print("1. Division\n2. Multiplication\n3. Mid-Square\n4. Folding")
    choice = int(input("Enter choice (1-4): "))
    methods = {1: "division", 2: "multiplication", 3: "mid_square", 4: "folding"}
    method = methods.get(choice, "division")
    for key in keys:
        hash_table.insert(key, method)
    print(f"\nHash Table using {method.title()} Method:\n")
    hash_table.display()

