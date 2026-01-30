def folding_hash(key, table_size):
    key_str = str(key)
    part_size = len(key_str) // 3
    parts = [int(key_str[i:i + part_size]) for i in range(0, len(key_str), part_size)]
    total = sum(parts)
    return total % table_size
if __name__ == "__main__":
    key = int(input("Enter key: "))
    table_size = int(input("Enter table size: "))
    
    hash_value = folding_hash(key, table_size)
    print(f"Key: {key}")
    print(f"Table Size: {table_size}")
    print(f"Hash Value: {hash_value}")
    print("Folding hashing completed successfully.")