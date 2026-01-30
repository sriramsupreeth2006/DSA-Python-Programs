def external_sort(arr, chunk_size):
    chunks = []
    i = 0
    while i < len(arr):
        chunk = arr[i:i+chunk_size]
        chunk.sort()
        chunks.append(chunk)
        i = i + chunk_size
    result = []
    indices = [0] * len(chunks)
    while True:
        min_val = None
        min_chunk = -1
        j = 0
        while j < len(chunks):
            if indices[j] < len(chunks[j]):
                val = chunks[j][indices[j]]
                if min_val is None or val < min_val:
                    min_val = val
                    min_chunk = j
            j = j + 1
        if min_chunk == -1:
            break
        result.append(min_val)
        indices[min_chunk] = indices[min_chunk] + 1
    return result
arr = list(map(int, input("Enter numbers separated by space: ").split()))
chunk_size = int(input("Enter chunk size: "))
sorted_arr = external_sort(arr, chunk_size)
print("Sorted array:", sorted_arr)
