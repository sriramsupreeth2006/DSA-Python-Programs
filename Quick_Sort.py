def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
try:
    n = int(input("Enter n value: "))
    cgpas = []
    for i in range(n):
        val = float(input(f"Enter CGPA of student {i+1} : "))
        cgpas.append(val)
    quick_sort(cgpas, 0, n - 1)
    sorted_str = " ".join(map(lambda x: str(int(x) if x.is_integer() else x), cgpas))
    print(f"Sample Output: The CGPA of students in order {sorted_str}")
except ValueError:
    print("Please enter valid numerical values.")