from collections import defaultdict

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]
    is_linked = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if computers[i][j]:
                    is_linked[i].append(j)
    for k in range(n):
        if visited[k]:
            continue
        else:
            visited[k] = 1
            stack = [k]
            while stack:
                p = stack.pop()
                for q in is_linked[p]:
                    if visited[q]:
                        continue
                    else:
                        stack.append(q)
                        visited[q] = 1
            answer += 1
    return answer