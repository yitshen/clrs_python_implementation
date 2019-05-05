'''
counting sort:
you need to know the maximum k
for non negative integer only
1. count list (length = k+1): count the frequency of the numbers
2. count[iii] += count[iii-1]: the positions
3. scan input list, put numbers to the right position

***stable sort algorithm meaning***
https://stackoverflow.com/questions/1517793/what-is-stability-in-sorting-algorithms-and-why-is-it-important

Stable Sorting Algorithms:
Insertion Sort
Merge Sort
Bubble Sort
Tim Sort
Counting Sort

Unstable Sorting Algorithms:
Heap Sort
Selection sort
Shell sort
Quick Sort
'''

def counting_sort(input, range_max):
    count = [0]*(range_max+1)
    output = [0]*len(input)
    for iii in input:
        count[iii] += 1
    for iii in range(1, len(count)):
        count[iii] += count[iii-1]
    for jjj in input[::-1]:
        output[count[jjj]-1] = jjj
        count[jjj] -= 1
    return output
test = [3,1,7,8,4,9]
# for jjj in
counting_sort(test,10)
