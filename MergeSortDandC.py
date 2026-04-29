def merge(arr, left, mid, right):
    # Create temporary arrays for the two halves
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    # Merge the temporary arrays back into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
    # Print the current state of the array as per the task requirement
    print(" ".join(map(str, arr)))

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge(arr, left, mid, right)

# --- Execution Logic ---
try:
    # Read input N (number of elements)
    n = int(input().strip())
    # Read the space-separated integers
    array_elements = list(map(int, input().split()))

    # Apply Merge Sort
    if n > 0:
        merge_sort(array_elements, 0, n - 1)

except EOFError:
    pass