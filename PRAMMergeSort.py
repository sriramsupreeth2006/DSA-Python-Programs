def odd_even_merge(left, right):
    n = len(left) + len(right)
    if n == 1:
        return left + right
    if n == 2:
        return sorted(left + right)

    # Recursive step: Merge odd-indexed and even-indexed elements
    odd_merged = odd_even_merge(left[0::2], right[0::2])
    even_merged = odd_even_merge(left[1::2], right[1::2])

    # Interleave results
    result = [None] * n
    result[0::2] = odd_merged
    result[1::2] = even_merged

    # Final parallel comparison and swap (Odd-Even adjustment)
    for i in range(1, n - 1, 2):
        if result[i] > result[i + 1]:
            result[i], result[i + 1] = result[i + 1], result[i]
    
    return result

def pram_merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    # Divide step
    left = pram_merge_sort(arr[:mid])
    right = pram_merge_sort(arr[mid:])
    
    # Parallel Merge step
    return odd_even_merge(left, right)

# Execution
if __name__ == "__main__":
    print("Enter unsorted numbers separated by space:")
    unsorted_list = list(map(int, input().split()))
    sorted_list = pram_merge_sort(unsorted_list)
    print("Sorted list:", sorted_list)