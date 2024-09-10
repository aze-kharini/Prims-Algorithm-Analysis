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
            while bIndex <= end and listRef[min(end, bIndex)] <= listRef[pivot]:
                bIndex += 1
            # bigger element found or hit the end of the list
            while listRef[pivot] <= listRef[sIndex] and sIndex > pivot:
                sIndex -=1
            # smaller element found or hit the pivot
            if bIndex < sIndex:
                listRef[bIndex], listRef[sIndex] = listRef[sIndex], listRef[bIndex]
                bIndex += 1
                sIndex -= 1
        # sindex should now be swapped or the same as the pivot
        listRef[sIndex], listRef[pivot] = listRef[pivot], listRef[sIndex]
        _quicksort(listRef, pivot, sIndex)
        _quicksort(listRef, sIndex+1, end)

'''
left_child = 2*n + 1
right_child = 2*n + 2
parent = (n-1)//2
'''

def _bubble_up(list_ref, i):
    value = list_ref[i]
    current_index = i
    parent_index = (current_index-1)//2
    while list_ref[parent_index] < value and current_index > 0:
        list_ref[parent_index], list_ref[current_index] = list_ref[current_index], list_ref[parent_index]
        current_index = parent_index
        parent_index = (current_index-1)//2

def _bubble_down(list_ref, heap_size):
    current_index = 0
    value = list_ref[0]
    left_child_index = 2*current_index + 1
    right_child_index = left_child_index + 1
    while left_child_index <= heap_size-1:
        new_index = left_child_index
        if right_child_index <= heap_size-1:
            if list_ref[left_child_index] < list_ref[right_child_index]:
                new_index = right_child_index
        if list_ref[new_index] > value:
            list_ref[new_index], list_ref[current_index] = list_ref[current_index], list_ref[new_index]
        else:
            break
        current_index = new_index
        left_child_index = 2*current_index + 1
        right_child_index = left_child_index + 1

def heapsort(list_ref):
    for i in range(len(list_ref)):
        _bubble_up(list_ref, i)
    heap_size = len(list_ref)-1
    for i in range(len(list_ref)):
        list_ref[0], list_ref[heap_size] = list_ref[heap_size], list_ref[0]
        _bubble_down(list_ref, heap_size)
        heap_size-=1

def insertionsort(list_ref):
    n = len(list_ref) 
    i = 1   # size of the sorted list / index of the next unsorted element
    while i < n:
        j = i-1 # j holds the index of the element immediately smaller than list_ref[i]
        while list_ref[i] < list_ref[j] and j > -1: # could be sped up with binary search? 
            j -= 1
        #insert i in the cell after j with shuffling
        temp = list_ref[i]  # holds the element which we are sorting now
        k = i-1 # holds the size of the sorted array
        while k > j:
            list_ref[k+1] = list_ref[k] # shifts the element to the right until it hits the last one larger than temp
            k -= 1
        list_ref[k+1] = temp
        i += 1 

def mergesort(mylist):
    n = len(mylist)
    if n>1:
        list1 = mylist[n//2:]
        list2 = mylist[:n//2]
        mergesort(list1)
        mergesort(list2)
        _merge(list1, list2, mylist)

def _merge(list1, list2, mylist):
    i1 = 0
    i2 = 0
    while i1 + i2 < len(mylist):
        if i1 == len(list1):
            mylist[i1+i2]=list2[i2]
            i2 +=1
        elif i2 == len(list2):
            mylist[i1+i2]=list1[i1]
            i1+=1
        elif list1[i1]>list2[i2]:
            mylist[i1+i2]=list2[i2]
            i2 +=1
        else:
            mylist[i1+i2]=list1[i1]
            i1+=1
