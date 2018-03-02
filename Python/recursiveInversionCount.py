# Recursive Inversion Count 

from readData import readArray


def mergeCount(seq, start, middle, end):
    assert 0 <= start < middle < end <= len(seq)
    inversions = 0
    temp = []
    i = start
    j = middle
    while i < middle and j < end:
        if seq[i] <= seq[j]:
            temp.append(seq[i])
            i += 1
        else:
            temp.append(seq[j])
            j += 1
            inversions += middle - i
    if j == end:
        # Second subsequence is complete
        temp.extend(seq[i:middle])
    else:
        # First subsequence is complete: no need to process
        # remaininder of second, since it does not move.
        pass
    # Insert sorted results into original sequence.
    seq[start:start+len(temp)] = temp
    return inversions

def sortCountInv(seq):
    
    def sortCount(seq, start, end):
        if end - start < 2:
            return 0
        middle = (start + end) // 2
        return (sortCount(seq, start, middle)
                + sortCount(seq, middle, end)
                + mergeCount(seq, start, middle, end))
    return sortCount(seq, 0, len(seq))


def main():
    print sortCountInv(readArray("data/integerArray.txt"))

if __name__ == '__main__':
    main()

