import heapq

def solution(jobs):
    q = []
    answer, now, counter = 0, 0, 0
    start = -1
    length = len(jobs)
    while counter < length:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(q,(job[1], job[0]))
            
        if q:
            time, request = heapq.heappop(q)
            start = now
            now += time
            answer += (now-request)
            counter += 1
        else:
            now += 1
            
    answer //= length
    return answer