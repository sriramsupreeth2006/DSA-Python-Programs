def mid_square(k, table_size):
    sq = k * k
    sq_str = str(sq)
    length = len(sq_str)

    if length < 3:
        mid_digits = sq_str
    else:
        mid = length // 2
        if length % 2 == 0:
            mid_digits = sq_str[mid-1:mid+1]
        else:
            mid_digits = sq_str[mid-1:mid+2]

    return int(mid_digits) % table_size

if __name__ == "__main__":
    k = list(map(int, input("Enter keys separated by space: ").split()))
    table_size = int(input("Enter table size: "))

    print(f"\nKeys: {k}")
    print(f"Table Size: {table_size}\n")

    for key in k:
        hash_value = mid_square(key, table_size)
        print(f"Key: {key}")
        print(f"Key Square: {key * key}")
        print(f"Hash Value: {hash_value}")
        print("Division hashing completed successfully.\n")
