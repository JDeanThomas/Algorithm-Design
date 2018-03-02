from readData import readArray

#  Algorithm to count inversions of integers and sort in place
# (or assignment to new sorted array)   

def inversionCount(array):
    return sortCountHelper(array, 0, len(array))
    
def sortCountHelper(array, left, right):
    if right - left < 2:
        return 0
    mid = (left + right) // 2
    return (sortCountHelper(array, left, mid)
            + sortCountHelper(array, mid, right)
            + mergeSortCount(array, left, mid, right))
    

def mergeSortCount(array, left, mid, right):
    assert 0 <= left < mid < right <= len(array)
    inversions = 0
    temp = []
    i = left
    j = mid
    while i < mid and j < right:
        if array[i] <= array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
            inversions += mid - i
    if j == right:
        temp.extend(array[i:mid])
    else:
        pass
        
    array[left:left+len(temp)] = temp
    return inversions


def main():
    array = inversionCount(readArray("data/integerArray.txt"))
    print array

if __name__ == '__main__':
    main()