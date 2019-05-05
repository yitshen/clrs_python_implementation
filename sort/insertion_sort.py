def insertion_sort(input, ascending = True):
    for iii in range(1, len(input)):
        key  = input[iii]
        while iii > 0 and key < input[iii-1]:
            input[iii-1], input[iii] = input[iii], input[iii-1]
            iii -= 1
    if ascending:
        return input
    else:
        return input[::-1]
test = [1,4,7,9,0,6]
insertion_sort(test)
