def remove_duplicates(s):
    seen = set()
    result = []
    
    for char in s:
        # Sets provide O(1) average lookup time
        if char not in seen:
            seen.add(char)
            result.append(char)
            
    return "".join(result)

# Reading input
if __name__ == "__main__":
    import sys
    # Using sys.stdin.read for faster input handling on large strings
    input_data = sys.stdin.read().strip()
    if input_data:
        print(remove_duplicates(input_data))