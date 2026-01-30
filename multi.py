def hash(k, s):
    return k % s
if __name__ == "__main__":
    keys = list(map(int, input("Enter keys separated by space: ").split()))
    table_size = int(input("Enter table size: "))

    print("Division Remainder method:")
    print(f"hash table size: {table_size}\n")
    for key in keys:
        hash_value = hash(key, table_size)
        print(f"Key: {key}, Hash Value: {hash_value}")
        # collision happens in this case 