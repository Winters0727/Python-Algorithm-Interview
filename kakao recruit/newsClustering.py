from collections import Counter

def solution(str1, str2):
    low_str1, low_str2 = str1.lower(), str2.lower()
    str1_list, str2_list = [low_str1[i:i+2] for i in range(len(low_str1)-1) if low_str1[i].isalpha() and low_str1[i+1].isalpha()], [low_str2[i:i+2] for i in range(len(low_str2)-1) if low_str2[i].isalpha() and low_str2[i+1].isalpha()]
    str1_set, str2_set = set(str1_list), set(str2_list)
    str_intersect = str1_set.intersection(str2_set)
    str_union = str1_set.union(str2_set)
    intersect, union = 0, 0
    str1_count, str2_count = Counter(str1_list), Counter(str2_list)
    for case in str_union:
        if case in str_intersect:
            intersect += min(str1_count[case], str2_count[case])
        union += max(str1_count[case], str2_count[case])
    if union:
        if intersect:
            result = intersect/union
        else:
            result = 0
    else:
        result = 1
    answer = int(result * 65536)
    return answer