def count_occurrences(arr, low, high, K):
    # Base Case: If there is only one element
    if low == high:
        if arr[low] == K:
            return 1
        else:
            return 0

    # Divide: Find the midpoint
    mid = (low + high) // 2

    # Conquer: Recursively count K in the left and right halves
    left_count = count_occurrences(arr, low, mid, K)
    right_count = count_occurrences(arr, mid + 1, high, K)

    # Combine: Return the sum of counts from both halves
    return left_count + right_count

# --- Execution based on provided image task ---
try:
    # Sample Input 1
    arr1 = [1, 1, 2, 2, 2, 2, 3]
    K1 = 1
    print(f"Input: arr[] = {arr1}, K = {K1}")
    print(f"Output: {count_occurrences(arr1, 0, len(arr1) - 1, K1)}")

    # Sample Input 2
    arr2 = [1, 1, 2, 2, 2, 2, 3]
    K2 = 4
    print(f"\nInput: arr[] = {arr2}, K = {K2}")
    print(f"Output: {count_occurrences(arr2, 0, len(arr2) - 1, K2)}")

except Exception as e:
    print(f"An error occurred: {e}")