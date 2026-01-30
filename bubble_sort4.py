array = list(map(int, input("Enter list of elements: ").split()))
length_array = len(array)
for i in range(length_array):
    for j in range(length_array - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(f"Sorted array: {array}")
