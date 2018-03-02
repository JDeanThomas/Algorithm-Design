from readData import readArray

# Function to merge-sort passed array of integers in place
# (or assignment to new sorted array)   
        
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array 


def main():
    array = mergeSort(readArray("data/integerArray.txt"))
    print array

if __name__ == '__main__':
    main()



    
        
        
        
        
        