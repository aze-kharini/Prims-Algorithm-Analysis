from random import randint

def quicksort(listRef):
    n = len(listRef)
    # shuffle the list
    for i in range(n):
        j = randint(0,n-1)
        listRef[i], listRef[j] = listRef[j], listRef[i]
    _quicksort(listRef, 0, n-1)

def _quicksort(listRef, pivot, end):
    if end - pivot > 0:
        bIndex = pivot + 1
        sIndex = end
        while bIndex <= sIndex:
            while bIndex <= end and listRef[min(end, bIndex)] < listRef[pivot]:
                bIndex += 1
            # bigger element found or hit the end of the list
            while listRef[pivot] < listRef[sIndex] and sIndex > pivot:
                sIndex -=1
            # smaller element found or hit the pivot
            if bIndex < sIndex:
                listRef[bIndex], listRef[sIndex] = listRef[sIndex], listRef[bIndex]
        # sindex should now be swapped or the same as the pivot
        listRef[sIndex], listRef[pivot] = listRef[pivot], listRef[sIndex]
        _quicksort(listRef, pivot, sIndex)
        _quicksort(listRef, sIndex+1, end)


if __name__ == "__main__":
    testList = [1, 0]
    quicksort(testList)
    print(testList)
