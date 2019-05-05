
'''
bucket sort
'''
import insertion_sort

# def insertion_sort(input):
#     for iii in range(1, len(input)):
#         key  = input[iii]
#         while iii > 0 and key < input[iii-1]:
#             input[iii-1], input[iii] = input[iii], input[iii-1]
#             iii -= 1
#     return input

def bucket_sort(input):
    import math
    n = len(input)
    temp = [[] for x in range(n)]
    for iii in range(n):
        temp[math.floor(n*input[iii])].append(input[iii])
    result = []
    for iii in range(n):
        if temp[iii] != []:
            result += insertion_sort(temp[iii])
    return result

test = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
bucket_sort(test)
