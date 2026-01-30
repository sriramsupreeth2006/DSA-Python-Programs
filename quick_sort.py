def partition_quick(arr, lower, higher):
    pivot = arr[lower]
    left_side = lower + 1
    right_side = higher
    while True:
        while left_side <= right_side and arr[left_side] <= pivot:
            left_side += 1
        while left_side <= right_side and arr[right_side] > pivot:
            right_side -= 1
        if left_side > right_side:
            break
        arr[left_side], arr[right_side] = arr[right_side], arr[left_side]
    arr[lower], arr[right_side] = arr[right_side], arr[lower]
    return right_side
def quick_sort(arr, lower, higher):
    if lower < higher:
        pi_q = partition_quick(arr, lower, higher)
        quick_sort(arr, lower, pi_q - 1)
        quick_sort(arr, pi_q + 1, higher)
arr = list(map(int, input("Enter elements: ").split()))
print(arr)
length = len(arr)
quick_sort(arr, 0, length - 1)
print(arr)
