def longest_common_subsequence(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    len_list = [[0]*(s2_len+1)]
    marker_list = [['']*(s2_len+1)]
    for iii in range(s1_len):
        len_list.append([0]*(s2_len+1))
        marker_list.append(['']*(s2_len+1))
        for jjj in range(s2_len):
            if s1[iii] == s2[jjj]:
                len_list[iii+1][jjj+1] = len_list[iii][jjj]+1
                marker_list[iii+1][jjj+1] = 'UL'
            elif len_list[iii][jjj+1] >= len_list[iii+1][jjj]:
                len_list[iii+1][jjj+1] = len_list[iii][jjj+1]
                marker_list[iii+1][jjj+1] = 'U'
            else:
                len_list[iii+1][jjj+1] = len_list[iii+1][jjj]
                marker_list[iii+1][jjj+1] = 'L'
    # return len_list, marker_list
    return len_list, marker_list

def print_lcs(s1, marker, i , j):
    subsequence = ''
    if i == 0 or j == 0:
        return subsequence
    if marker[i][j] == 'UL':
        subsequence = s1[i-1] + subsequence
        return print_lcs(s1, marker, i-1, j-1)+subsequence
    elif marker[i][j] == 'L':
        return print_lcs(s1, marker, i, j-1)+ subsequence
    else:
        return print_lcs(s1, marker,i-1, j)+subsequence

if __name__ == '__main__':
    s1 = input('Please input the first sequence:\n')
    s2 = input('Please input the second sequence:\n')
    len_list, marker = longest_common_subsequence(s1, s2)
    print('The length of the longest common subsequence is {}.'.format(len_list[-1][-1]))
    print(print_lcs(s1, marker, len(marker)-1, len(marker[0])-1))
