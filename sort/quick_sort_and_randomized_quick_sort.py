
"""
chapter 7: quick sort
1. for a list ,divide the list into two parts:
left part <= the last element of the list
right part > the last element of the list
2. quick sort the two parts
worst: O(n^2)
best: O(n logn)

randomized quick sort:
choose the pivot element using random numbers to avoid the worst case

"""
# def quick_sort(input):

import random
def randomized_partition(temp, l, r):
    pivot = random.randint(l, r)
    temp[pivot], temp[r] = temp[r], temp[pivot]
    return partition(temp, l, r)

def randomized_quick_sort(A, l, r):
    if r>l:
        q = randomized_partition(A, l, r)
        randomized_quick_sort(A, l, q-1)
        randomized_quick_sort(A, q+1, r)

def partition(temp, l, r):
    x = temp[r]
    iii = l-1
    for jjj in range(l, r):
        if temp[jjj] <= x:
            iii += 1
            temp[jjj], temp[iii] = temp[iii], temp[jjj]
    temp[iii+1], temp[r] = temp[r], temp[iii+1]
    return iii+1

def quick_sort(A, l, r):
    if r>l:
        q = partition(A, l, r)
        quick_sort(A, l, q-1)
        quick_sort(A, q+1, r)
