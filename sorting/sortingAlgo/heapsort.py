

'''
left_child = 2*n + 1
right_child = 2*n + 2
parent = (n-1)//2
'''

def bubble_up(list_ref, i):
    value = list_ref[i]
    current_index = i
    parent_index = (current_index-1)//2
    while list_ref[parent_index] < value and current_index > 0:
        list_ref[parent_index], list_ref[current_index] = list_ref[current_index], list_ref[parent_index]
        current_index = parent_index
        parent_index = (current_index-1)//2

def bubble_down(list_ref, heap_size):
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

def heapSort(list_ref):
    for i in range(len(list_ref)):
        bubble_up(list_ref, i)
    heap_size = len(list_ref)-1
    for i in range(len(list_ref)):
        list_ref[0], list_ref[heap_size] = list_ref[heap_size], list_ref[0]
        bubble_down(list_ref, heap_size)
        heap_size-=1

