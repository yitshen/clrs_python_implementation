# merge two sorted list:
def merge_two_sorted_list(list1, list2):
    list_merged = []
    iii1 = 0
    iii2 = 0
    while iii1 < len(list1) and iii2 < len(list2):
        list_merged.append(min(list1[iii1], list2[iii2]))
        if list1[iii1] > list2[iii2]:
            iii2 += 1
        else:
            iii1 += 1
    return list_merged + list1[iii1:] + list2[iii2:]

def merge_sort(input):
    while len(input) > 1:
        list1 = input[0:int(len(input)/2)]
        list2 = input[int(len(input)/2):]
        return merge_two_sorted_list(merge_sort(list1), merge_sort(list2))
    return input
