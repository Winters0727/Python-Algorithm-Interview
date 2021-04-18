from bisect import bisect_left

bisect_left()

def solution(n, times):
    times.sort()
    workers = len(times)
    if n < workers:
        return sum(times[:n])
    answer = 0
    return answer