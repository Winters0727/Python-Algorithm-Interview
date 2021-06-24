def solution(lottos, win_nums):
    check_counter = 0
    zero_counter = 0
    
    for num in lottos:
        if num in win_nums:
            check_counter += 1
        if num == 0:
            zero_counter += 1
    if zero_counter == 6:
        return [1,6]
    
    if check_counter < 2:
        temp_rank = 6
    else:
        temp_rank = 7-check_counter
    answer = [temp_rank-zero_counter, temp_rank]
    return answer