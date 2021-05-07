from collections import deque

def solution(play_time, adv_time, logs):
    def string_to_time(string):
        h, m, s = map(int, string.split(':'))
        return h*3600 + m*60 + s
    
    def time_to_string(time):
        div, s = divmod(time, 60)
        h, m = divmod(div, 60)
        return '{0}:{1}:{2}'.format(str(h).zfill(2),str(m).zfill(2),str(s).zfill(2))
    
    play_time = string_to_time(play_time)
    adv_time = string_to_time(adv_time)

    if play_time <= adv_time:
        return time_to_string(0)

    all_time = [0 for _ in range(play_time+1)]
    
    for log in logs:
        s, e = log.split('-')
        all_time[string_to_time(s)] += 1
        all_time[string_to_time(e)] -= 1

    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]

    for i in range(1, play_time+1):
        all_time[i] += all_time[i-1]
    
    max_count, max_time = 0, 0
    for start in range(play_time-adv_time+1):
        temp_count = all_time[start+adv_time] - all_time[start]
        if temp_count > max_count:
            max_count = temp_count
            if start:
                max_time = start+1
            else:
                max_time = start
    answer = time_to_string(max_time)
    return answer