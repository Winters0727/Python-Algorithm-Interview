import heapq

def solution(operations):
    queue = []
    min_pop, max_pop = 0, 0
    for oper in operations:
        command, value = oper.split(' ')
        if command == 'I':
            heapq.heappush(queue, int(value))
        elif command == 'D':
            if value == '1':
                max_pop += 1
            else:
                min_pop += 1
    for _ in range(min_pop):
        if queue:
            print(queue)
            heapq.heappop(queue)

    queue = [-num for num in queue]

    for _ in range(max_pop):
        if queue:
            heapq.heappop(queue)
    
    queue = [-num for num in queue]

    answer = [0, 0]
    queue.sort()
    if queue:
        answer = [min(queue), max(queue)]
    return answer