#Insertion Sort
def insertion_sort(array):
    length_of_array = len(array)
    for a in range(1, length_of_array):
        key = array[a]
        b = a - 1
        while b >= 0:
            if key < array[b]:
                array[b + 1] = array[b]
                b -= 1
            else:
                break
        array[b + 1] = key
array = list(map(int, input("Enter list with spaces: ").split()))
print(array)
insertion_sort(array)
print(array)
