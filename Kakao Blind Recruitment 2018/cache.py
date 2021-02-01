from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()
    for city in cities:
        low_city = city.lower()
        if low_city in queue:
            answer += 1
            queue.remove(low_city)
            queue.appendleft(low_city)
        else:
            answer += 5
            queue.appendleft(low_city)
            if len(queue) > cacheSize:
                queue.pop()
    return answer