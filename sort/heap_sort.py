'''
Chapter 6_heap sort
1. max_heapify (assume both left and right has already max_heapified, O(lg n)， root is the largest number)
2. build max heap: max heapify from the parent of the last leaf, O(n lg n)......root is maximum, everything else max_heapify
3. Sort: build max heap; exchange root and last heap element; reduce heap size by 1, max_heapified the rest of the heap.

'''

def left(iii):
    return 2*iii+1
def right(iii):
    return 2*iii+2
def parent(iii):
    import math
    return math.ceil(iii/2)-1

def max_heapify(input_list, index, heapsize):
    largest = index
    l = left(index)
    r = right(index)
    if l <= heapsize-1 and input_list[index] < input_list[l]:
        largest = l
    if r <= heapsize-1 and input_list[largest] < input_list[r]:
        largest = r
    if largest != index:
        input_list[index], input_list[largest] = input_list[largest], input_list[index]
        max_heapify(input_list, largest, heapsize)
    return input_list

test = [16, 4,10,14,7,9,3,2,8,1]
max_heapify(test,1, len(test))

def build_max_heap(A):
    for iii in range(parent(len(A)-1),-1,-1):
        max_heapify(A,iii, len(A))
    return A
test = [4, 1,3,2,16,9,10,14,8,7]
build_max_heap(test)

def heap_sort(A):
    build_max_heap(A)
    for iii in range(len(A),1,-1):
        A[iii-1], A[0] = A[0], A[iii-1]
        # A = A[:-1]
        # heapsize -= 1
        max_heapify(A,0, iii-1)
    # B.append(A[0])
    return A
test = [4,1,3,2,16,9,10,14,8,7]
heap_sort(test)



'''
Chapter 6_heap sort
1. max_heapify (assume both left and right has already max_heapified, O(log n))
2. build max heap: max heapify from the parent of the last leaf, O(nlogn)......root is maximum, everything else max_heapify
3. Sort: build max heap; exchange root and last heap element; reduce heap size, max_heapified the rest of the heap.

'''
def left(iii):
    return 2*iii+1
def right(iii):
    return 2*iii+2
def parent(iii):
    import math
    return math.ceil(iii/2)-1

def max_heapify(input_list, index, heapsize):
    largest = index
    l = left(index)
    r = right(index)
    if l <= heapsize-1 and input_list[index] < input_list[l]:
        largest = l
    if r <= heapsize-1 and input_list[largest] < input_list[r]:
        largest = r
    if largest != index:
        input_list[index], input_list[largest] = input_list[largest], input_list[index]
        max_heapify(input_list, largest, heapsize)
    return input_list
test = [16, 4,10,14,7,9,3,2,8,1]
max_heapify(test,1, len(test))

def build_max_heap(A):
    for iii in range(parent(len(A)-1),-1,-1):
        max_heapify(A,iii, len(A))
    return A
test = [4, 1,3,2,16,9,10,14,8,7]
build_max_heap(test)

def heap_sort(A):
    build_max_heap(A)
    # B = []
    # heapsize = len(A)
    for iii in range(len(A),1,-1):
        A[iii-1], A[0] = A[0], A[iii-1]
        # A = A[:-1]
        # heapsize -= 1
        max_heapify(A,0, iii-1)
    # B.append(A[0])
    return A
test = [4,1,3,2,16,9,10,14,8,7]
heap_sort(test)
