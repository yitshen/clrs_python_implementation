import numpy as np

def selection_sort(input, ascending = True):
    for iii in range(len(input)-1):
        min_index = np.argmin(input[iii:])+iii
        if min_index != iii:
            input[iii], input[min_index] = input[min_index], input[iii]
    if ascending:
        return input
    else:
        return input[::-1]
