from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    path = defaultdict(list)
    for e in edge:
        path[e[0]].append(e[1])
        path[e[1]].append(e[0])
    visited = [0 for _ in range(n)]
    visited[0] = 1
    max_count = 0
    q = deque([(1,0)])
    while q:
        node, count = q.popleft()
        for des in path[node]:
            if not visited[des-1]:
                visited[des-1] = 1
                q.append((des, count+1))
                if count+1 == max_count:
                    answer += 1
                elif count+1 > max_count:
                    max_count = count+1
                    answer = 1
    return answer