def mid_sqaure(k, table_size):
    sq = k * k
    sq_str = str(sq)
    length = len(sq_str)
    if length < 3:
        mid_digits = sq_str
    else:
        mid = length // 2
        if length % 2 == 0:
            mid_digits = sq_str[mid-1:mid+1]  # 2 digits
        else:
            mid_digits = sq_str[mid-1:mid+2]
    return int(mid_digits) % table_size

if __name__ == "__main__":
    k = int(input("Enter key: "))
    table_size = int(input("Enter table size: "))
    hash_value = mid_sqaure(k, table_size)
    print(f"Keys: {k}")
    print(f"Key Square: {k*k}")
    print(f"Table Size: {table_size}")
    print(f"Hash Value: {hash_value}")
    print("Division hashing completed successfully.")
