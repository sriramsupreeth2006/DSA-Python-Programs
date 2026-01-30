def hash(k,s):
 # This function computes the hash value using the division method.   
    return k % s
# Main function to demonstrate the hash function.e, so we can see how it handles collisions.
        # In a real application, you would
if __name__ == "__main__":
    # Get user input for keys and table size
    s = int(input("enter size:"))
    k = int(input("enter key:"))
    hash_value = hash(k, s)
    print(f"Key:{k}")
    print(f"Size:{s}")
    print(f"Hash value:{hash_value}")
    print("Hashing completed successfully.")
