'''
clrs dynamic programming example 1:
rod cutting problem
'''

def cut_rod(price_list, length):
    if length == 0:
        return 0
    revenue = -1
    for iii in range(1, length+1):
        revenue = max(revenue, price_list[iii]+cut_rod(price_list, length - iii))
    return revenue

price = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20, 9:24, 10:30}

cut_rod(price, 10)
