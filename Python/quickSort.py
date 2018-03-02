from readData import readArray

# Quick sort algorithm. Sorts array of integers to sort in place
# (or assignment to new sorted array)   

def quickSort(array):
    recursionHelper(array, 0 , len(array)-1)

def recursionHelper(array,first,last):
    if first < last:
        split = partition(array,first,last)
        recursionHelper(array,first,split-1)
        recursionHelper(array,split+1,last)

def partition(array,first,last):
    pivot = array[first]
    left = first+1
    right = last
    done = False
    while not done:
        while left <= right and array[left] <= pivot:
            left = left + 1
        while array[right] >= pivot and right >= left:
            right = right -1
        if right < left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
    temp = array[first]
    array[first] = array[right]
    array[right] = temp
    return right
    

def main():
    array = quickSort(readArray("data/integerArray.txt"))
    print array

if __name__ == '__main__':
    main()
    #import cProfile
    #cProfile.run("quickSort('data/integerArray.txt')")