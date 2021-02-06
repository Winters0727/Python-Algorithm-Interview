from collections import deque

def solution(n, t, m, timetable):
    copy_timetable = timetable[:]
    copy_timetable.sort(key=lambda x : [x.split(':')[0], x.split(':')[1]])
    my_table = deque(copy_timetable)
    print(my_table)
    answer = ''
    return answer