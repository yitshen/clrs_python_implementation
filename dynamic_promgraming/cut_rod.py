'''
clrs dynamic programming example 1:
rod cutting problem
'''
'''
recursive solution
O(2^n)
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

'''
bottom up
O(n^2)
'''
def bottom_up_cut_rod(price_list, length):
    revenue_list = [0]
    for iii in range(1, length+1):
        revenue = -1
        for jjj in range(1, iii+1):
            revenue = max(revenue, price_list[jjj]+revenue_list[iii - jjj])
        revenue_list.append(revenue)
    return revenue_list[length]
bottom_up_cut_rod(price, 10)

'''
memorization
'''
def memorized_cut_rod(price_list, length):
    revenue_list = [-1]*(length+1)
    return memorized_cut_rod_aux(price_list, length, revenue_list)
def memorized_cut_rod_aux(price_list, length, revenue_list):
    if revenue_list[length] >= 0:
        return revenue_list[length]
    if length == 0:
        q = 0
    else:
        q = -1
        for iii in range(1, length+1):
            q = max(q, price_list[iii] + memorized_cut_rod_aux(price_list, length-iii, revenue_list))
    revenue_list[length] = q
    return q
memorized_cut_rod(price, 9)
