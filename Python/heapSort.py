from readData import readArray

# Heap sort algorithm. Sorts array of integers to sort in place
# (or assignment to new sorted array)  

def heapSort(array):
    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        moveDown(array, 0, end)

def heapify(array, count):
    start = int((count - 2) / 2)
    while start >= 0:
        moveDown(array, start, count - 1)
        start -= 1

def moveDown(array, start, end):
    root = start
    while (root * 2 + 1) <= end:
        child = root * 2 + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if (child + 1) <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap != root:
            array[root], array[swap] = array[swap], array[root]
            root = swap
        else:
            return

def main():
    array = heapSort(readArray("data/integerArray.txt"))
    print array

if __name__ == '__main__':
    main()