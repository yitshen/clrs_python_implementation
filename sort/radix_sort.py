'''
combine radix sort and counting sort for O(n) Sorting
'''

def radix_sort(input_list):
    radix = 10
    largest_digit = False
    digit = 10
    while not largest_digit:
        largest_digit = True
        count = [0]*radix
        temp = [None]*len(input_list)
        digit_temp = [ iii%digit for iii in input_list]
        for iii in count:
            if iii!=0:
                largest_digit = False
                break
        for iii in digit_temp:
            count[iii] += 1
        for iii in range(1, len(count)):
            count[iii] = count[iii]+count[iii-1]
        for iii in range(len(digit_temp)-1, -1,-1):
            temp[count[digit_temp[iii]]-1] = input_list[iii]
            count[digit_temp[iii]] -= 1
        digit *= radix
        input_list = temp
    return input_list

test = [1,23,45,22]
radix_sort(test)
