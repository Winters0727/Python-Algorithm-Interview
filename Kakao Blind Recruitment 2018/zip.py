from collections import defaultdict

def solution(msg):
    answer = []
    
    my_dict = defaultdict(int)
    for i in range(65,91):
        my_dict[chr(i)] = i-64
    length = len(msg)
    start, sub_len = 0, 1
    
    while start + sub_len -1 < length:
        sub_msg = msg[start:start+sub_len]
        if sub_msg in my_dict.keys():
            sub_len += 1
            continue
        else:
            answer.append(my_dict[sub_msg[:-1]])
            my_dict[sub_msg] = len(my_dict.keys())+1
            start += sub_len -1
            sub_len = 1
    answer.append(my_dict[sub_msg])
    return answer