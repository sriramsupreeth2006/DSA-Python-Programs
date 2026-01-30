#Shell Sort
def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
print("Shell sort demo")
data = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original array:", data)
shell_sort(data)
print("Sorted array:", data)
