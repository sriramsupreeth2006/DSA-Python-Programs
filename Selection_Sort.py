def selection_sort(array):
    length_array = len(array)
    for i in range(length_array):
        minimum_index = i
        for j in range(i + 1, length_array):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]
            
data = list(map(int, input("Enter the data: ").split()))
print("Original data: ", data)
selection_sort(data)
print("Data in sorted order: ", data)
