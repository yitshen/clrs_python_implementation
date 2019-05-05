'''
insert number to a sorted list
time complexity O(n)
'''

def insert_num_sorted_list(sortedList, insertNum):
    if insertNum <= sortedList[0]:
        return [insertNum] + sortedList
    elif insertNum >= sortedList[-1]:
        return sortedList + [insertNum]
    else:
        for iii in range(len(sortedList)-1):
            if sortedList[iii] <= insertNum and sortedList[iii+1] >= insertNum:
                return sortedList[:iii+1] + [insertNum] + sortedList[iii+1:]
