
def insertionSort(list_ref):
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


