def merge(array, left, right):
    a = b = c = 0
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            array[c] = left[a]
            a += 1
        else:
            array[c] = right[b]
            b += 1
        c += 1
    while a < len(left):
        array[c] = left[a]
        a += 1
        c += 1
    while b < len(right):
        array[c] = right[b]
        b += 1
        c += 1
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(array, left, right)
data = list(map(int, input("Enter numbers: ").split()))
print(data)
merge_sort(data)
print(data)
