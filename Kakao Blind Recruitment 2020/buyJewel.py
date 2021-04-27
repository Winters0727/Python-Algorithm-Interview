from collections import defaultdict

def solution(gems):
    length = len(gems)
    answer = [1, 1]
    gems_dict = defaultdict(int)
    gems_length = len(gems_dict.keys())
    for idx, gem in enumerate(gems):
        gems_dict[gem] = idx
        temp_length = len(gems_dict.keys())
        if temp_length > 1:
            min_val, max_val = min(gems_dict.values())+1, max(gems_dict.values())+1
            if temp_length > gems_length or (max_val - min_val) < (answer[1] - answer[0]):
                gems_length = temp_length
                answer = [min_val, max_val]
    return answer