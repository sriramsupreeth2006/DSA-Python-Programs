def parent(i):
    return (i - 1) // 2
def leftchild(i):
    return ((2 * i) + 1)
def rightchild(i):
    return ((2 * i) + 2)
def shiftup(i, arr):
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]
        i = parent(i)
def shiftdown(i, arr, size):
    max_index = i
    l = leftchild(i)
    if l < size and arr[l] > arr[max_index]:
        max_index = l
    r = rightchild(i)
    if r < size and arr[r] > arr[max_index]:
        max_index = r
    if i != max_index:
        arr[i], arr[max_index] = arr[max_index], arr[i]
        shiftdown(max_index, arr, size)
def insert(p, arr, size):
    size[0] = size[0] + 1
    arr.append(p)
    shiftup(size[0] - 1, arr)
def extractmax(arr, size):
    res = arr[0]
    arr[0] = arr[size[0] - 1]
    arr.pop()
    size[0] = size[0] - 1
    shiftdown(0, arr, size[0])
    return res
def changepriority(i, p, arr, size):
    oldp = arr[i]
    arr[i] = p
    if p > oldp:
        shiftup(i, arr)
    else:
        shiftdown(i, arr, size[0])
def getmax(arr):
    return arr[0]
def remove(i, arr, size):
    arr[i] = getmax(arr) + 1
    shiftup(i, arr)
    extractmax(arr, size)
if __name__ == "__main__":
    arr=[]
    size = [0]
    insert(45, arr, size)
    insert(20, arr, size)
    insert(14, arr, size)
    insert(31, arr, size)
    insert(7, arr, size)
    i = 0
    print("Heap:", arr)
    print("Extracted max:", extractmax(arr, size))
    print("Heap after extract:", arr)
    