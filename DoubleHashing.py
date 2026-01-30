def H1(k):
    return k % 13
def H2(k):
    return 12 - (k % 12)
def double_hash_insert(table, key):
    size = len(table)
    h1 = H1(key)
    h2 = H2(key)
    for i in range(size):
        index = (h1 + i * h2) % size
        if table[index] is None:
            table[index] = key
            print(f"Inserted {key} at index {index}")
            return
        else:
            print(f"Collision at index {index} for key {key}")
    print("Hash Table Full! Could not insert", key)
if __name__ == "__main__":
    size = 13
    hash_table = [None] * size
    n = int(input("Enter number of keys: "))
    keys = list(map(int, input("Enter the keys (space separated): ").split()))
    if n != len(keys):
        print("Count is mismatching! Enter correct number of keys.")
    else:
        for k in keys:
            double_hash_insert(hash_table, k)
        print("\nFinal Hash Table:")
        print(hash_table)
