def partition(arr, low, high):
    # Choosing the rightmost element as pivot
    pivot = arr[high]
    
    # Pointer for greater element
    i = low - 1
    
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            
            # Swapping element at i with element at j
            arr[i], arr[j] = arr[j], arr[i]
            
    # Swap the pivot element with the greater element specified by i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Return the position from where partition is done
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        # Recursive call on the left of pivot
        quick_sort(arr, 0, pi - 1)
        
        # Recursive call on the right of pivot
        quick_sort(arr, pi + 1, high)

# --- Execution Logic ---
if __name__ == "__main__":
    # Example input to test the program
    data = [8, 7, 6, 1, 0, 9, 2]
    print(f"Unsorted Array: {data}")
    
    size = len(data)
    quick_sort(data, 0, size - 1)
    
    print(f"Sorted Array in Ascending Order: {data}")