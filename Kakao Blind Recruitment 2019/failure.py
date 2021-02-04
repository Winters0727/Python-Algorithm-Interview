from collections import Counter

def solution(N, stages):
    stage_count = Counter(stages)
    users = len(stages)
    failure = []
    for i in range(1, N+2):
        if i == N+1:
            break
        if users:
            failure.append(stage_count[i]/users)
        else:
            failure.append(0)
        users -= stage_count[i]
                      
    answer = [num for num in range(1, N+1)]
    if sum(failure):
        answer.sort(key = lambda x : failure[x-1], reverse=True)
    return answer