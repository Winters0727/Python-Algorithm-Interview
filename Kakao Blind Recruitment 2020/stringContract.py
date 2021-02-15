def solution(s):
    length = len(s)
    if length < 2:
        return length
        
    limit = len(s)//2
    answer_list = []
    for c in range(1, limit+1):
        temp_str, rear_str = '', s[:c]
        cur = c
        counter = 1
        while cur < length:
            next_str = s[cur:cur+c]
            if next_str == rear_str:
                counter += 1
            else:
                if counter > 1:
                    temp_str += ''.join([rear_str, str(counter)])
                else:
                    temp_str += rear_str
                rear_str = next_str
                counter = 1
            cur += c
        if counter > 1:
            temp_str += ''.join([rear_str, str(counter)])
        else:
            temp_str += rear_str
        answer_list.append(len(temp_str))
    answer = min(answer_list)
    return answer