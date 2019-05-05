'''
randamized select: get the ith smallest number
use randomized_partition and partition from quick sort
'''
import random

def randomized_partition(inputList,left, right):
    tempPivot = random.randint(left, right)
    inputList[right], inputList[tempPivot] = inputList[tempPivot], inputList[right]
    return partition(inputList, left, right)

def partition(inputList, left, right):
    pivot = inputList[right]
    iii = left-1
    for jjj in range(left, right):
        if inputList[jjj] <= pivot:
            iii += 1
            inputList[iii], inputList[jjj] = inputList[jjj], inputList[iii]
    inputList[iii+1], inputList[right] =     inputList[right], inputList[iii+1]
    return iii+1

def randomized_select(inputList, left, right, number):
    if left == right:
        return inputList[left]
    q = randomized_partition(inputList, left, right)
    if q-left == number-1:
        return inputList[q]
    elif q-left > number-1:
        return randomized_select(inputList, left, q-1, number)
    else:
        return randomized_select(inputList, q+1, right, number-q+left-1)
test = [1,2,3,4,5,6,0,8,4,5,6]
randomized_select([1,3,5,7,2,4,6,8,0], 0,8,6)
