#Quick Sort
def partition(array, low, high):
    pivot = array[low]
    left = low + 1
    right = high
    while True:
        while left <= right and array[left] <= pivot:
            left += 1
        while left <= right and array[right] > pivot:
            right -= 1
        if left > right:
            break
        array[left], array[right] = array[right], array[left]
    array[low], array[right] = array[right], array[low]
    return right
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)
array = list(map(int, input("Enter list with spaces: ").split()))
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
